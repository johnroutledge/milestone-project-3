import os
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MOGNO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
coin_market_cap_key = os.environ.get("COIN_MARKET_CAP_KEY")

mongo = PyMongo(app)


# this procedure retrieves the latest cryptocurrency prices via API call from
# coinmarketcap.com and returns it in JSON format in coins
def get_latest_prices():
    # code to get cryptocurrency prices adapted from Coding Under Pressure
    # YouTube channel 'How to Use an API in Python to get Bitcoin's Price
    # Live - Along with other Cryptocurrencies'
    headers = {
            'X-CMC_PRO_API_KEY': coin_market_cap_key,
            'Accepts': 'application/json'
    }

    params = {
        'start': '1',
        'limit': '30',
        'convert': 'USD'
    }

    try:
        url = ('https://pro-api.coinmarketcap.com/'
               'v1/cryptocurrency/listings/latest')
        json = requests.get(url, params=params, headers=headers).json()
        coins = json['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        flash(e)

    return coins


# this procedure returns a user's total portfolio balance
# by taking their balance for each cryptocurrency then
# multiplying it by its current price (taken from the api
# call) and finally adding them together
def get_total_balance(balances, coins):
    total_balance = 0
    dict = {}
    for balance in balances:
        if balance.upper() == "USD":
            x = balances[balance]
            dict[balance.upper()] = x
            total_balance = total_balance + float(x)
        else:
            for coin in coins:
                if coin['symbol'] == balance.upper():
                    x = coin['quote']['USD']['price'] * float(
                        balances[balance])
                    x = "{:.2f}".format(x)
                    dict[balance.upper()] = x
                    total_balance = total_balance + float(x)

    return total_balance


@app.route("/")
def home():
    if "user" not in session:
        current_user = "none"
    else:
        current_user = session["user"]
    
    return render_template("index.html", current_user=current_user)


@app.route("/get_currencies")
def get_currencies():
    currencies = mongo.db.currencies.find()
    coins = get_latest_prices()
    return render_template(
        "currencies.html", currencies=currencies, coins=coins)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if email already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("email already registered")
            return redirect(url_for("register"))

        date_today = time_stamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        # date_today = datetime.now().strftime('%d-%m-%Y')
        register = {
            "first_name": request.form.get("first_name").capitalize(),
            "last_name": request.form.get("last_name").capitalize(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password").lower()),
            "register_date": date_today
        }
        # need to refactor
        balances = {
            "email": request.form.get("email").lower(),
            "usd": 100000,
            "btc": 0,
            "eth": 0,
            "doge": 0,
            "ada": 0,
            "ltc": 0,
            "xrp": 0,
            "usdt": 0,
            "bnb": 0,
            "sol": 0,
            "dot": 0,
            "avax": 0,
            "xlm": 0,
            "uni": 0,
            "luna": 0,
            "link": 0,
            "algo": 0,
            "shib": 0
        }
        mongo.db.users.insert_one(register)
        mongo.db.balances.insert_one(balances)

        # put the new user into session cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful")
        return redirect(url_for("portfolio", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if email already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # make sure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Hi {}".format(
                    existing_user["first_name"].capitalize()))
                return redirect(
                    url_for("portfolio", username=session["user"]))
            else:
                # incorrect password
                flash("Incorrect email and/or password")
                return redirect(url_for("login"))

        else:
            # email doesn't exist
            flash("Incorrect email and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/settings/")
def settings():
    # this redirects user to login screen if not logged in
    if "user" not in session:
        return redirect(url_for("login"))

    # get users first name from db
    user_settings = mongo.db.users.find_one(
        {"email": session["user"]})

    # get users balances from db
    balances = mongo.db.balances.find_one(
        {"email": session["user"]})

    # retrieve the latest crypto prices
    coins = get_latest_prices()

    # create a dictionary which calculate the user's
    # balance for each cryptocurrency
    total_balance = get_total_balance(balances, coins)

    if session["user"]:
        return render_template(
            "settings.html", user_settings=user_settings,
            portfolioBalance=total_balance)


@app.route("/edit_settings/", methods=["GET", "POST"])
def edit_settings():
    # this redirects user to login screen if not logged in
    if "user" not in session:
        return redirect(url_for("login"))

    # get users first name from db
    user_settings = mongo.db.users.find_one(
        {"email": session["user"]})

    if request.method == "POST":
        mongo.db.users.update(
            {"email": session["user"]},
            {"$set":
                {
                    "first_name": request.form.get("first_name"),
                    "last_name": request.form.get("last_name"),
                    "display_currency": request.form.get("display_currency")
                }
             }
        )
        flash("Settings Successfully Updated")
        # need to refactor
        if request.form.get("reset_account") == "on":
            # delete all transaction records for user from db
            mongo.db.transactions.remove({"email": session["user"]})
            # reset user portfolio balances
            mongo.db.balances.update(
                {"email": session["user"]},
                {"$set":
                    {
                        "usd": 100000,
                        "btc": 0,
                        "eth": 0,
                        "doge": 0,
                        "ada": 0,
                        "ltc": 0,
                        "xrp": 0,
                        "usdt": 0,
                        "bnb": 0,
                        "sol": 0,
                        "dot": 0,
                        "avax": 0,
                        "xlm": 0,
                        "uni": 0,
                        "luna": 0,
                        "link": 0,
                        "algo": 0,
                        "shib": 0
                    }
                 }
            )
            flash("Account reset")

        return redirect(url_for("settings"))

    if session["user"]:
        return render_template(
            "edit_settings.html", user_settings=user_settings)


@app.route("/portfolio/")
def portfolio():
    # this redirects user to login screen if not logged in
    if "user" not in session:
        return redirect(url_for("login"))

    # get users first name from db
    username = mongo.db.users.find_one(
        {"email": session["user"]})["first_name"]

    if session["user"]:
        # retrieve user's balance for each cryptocurrency
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})

        member_since = mongo.db.users.find_one(
            {"email": session["user"]})["register_date"]
        
        # retrieve user's details from users document
        user = mongo.db.users.find_one(
            {"email": session["user"]})
        
        # convert member_since from string to required date format
        member_since = datetime.strptime(member_since, '%d-%m-%Y %H:%M:%S')
        member_since = member_since.strftime('%d-%b-%Y')

        # retrieve all tradable cryptocurrencies
        currencies = mongo.db.currencies.find()

        # retrieve latest cryptocurrency prices
        coins = get_latest_prices()

        # create a dictionary which calculates the user's
        # USD balance for each cryptocurrency
        dict = {}
        total_balance = 0
        percentage_change = 0
        for balance in balances:
            if balance.upper() == "USD":
                x = balances[balance]
                dict[balance.upper()] = x
                total_balance = total_balance + float(x)
            else:
                for coin in coins:
                    if coin['symbol'] == balance.upper():
                        x = coin['quote']['USD']['price'] * float(
                            balances[balance])
                        x = "{:.2f}".format(x)
                        dict[balance.upper()] = x
                        total_balance = total_balance + float(x)

            percentage_change = "{:.2f}".format(
                (total_balance - 100000) / 1000)

        return render_template(
            "portfolio.html", username=username,
            currencies=currencies, balances=balances, coins=coins,
            user=user, dict=dict, total_balance=total_balance,
            percentage_change=percentage_change, member_since=member_since)

    return redirect(url_for("login"))


@app.route("/transactions/")
def transactions():
    # this redirects user to login screen if not logged in
    if "user" not in session:
        return redirect(url_for("login"))

    # get users first name from db
    username = mongo.db.users.find_one(
        {"email": session["user"]})["first_name"]

    if session["user"]:
        # retrieve user's transaction history
        transactions = mongo.db.transactions.find(
            {"email": session["user"]})

        return render_template(
            "transactions.html", transactions=transactions)

    return redirect(url_for("login"))


@app.route("/trade/<ticker>", methods=["GET", "POST"])
def trade(ticker):
    # this redirects user to login screen if not logged in
    if "user" not in session:
        return redirect(url_for("login"))

    if session["user"]:
        # retrieve user's coin balance for each cryptocurrency
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})

        # retrieve all tradable cryptocurrencies
        currencies = mongo.db.currencies.find()
        coins = get_latest_prices()

        # create a dictionary which calculates the user's
        # USD balance for each cryptocurrency
        dict = {}
        total_balance = 0
        percentage_change = 0
        for balance in balances:
            if balance.upper() == "USD":
                x = balances[balance]
                dict[balance.upper()] = x
                total_balance = total_balance + float(x)
            else:
                for coin in coins:
                    if coin['symbol'] == balance.upper():
                        x = coin['quote']['USD']['price'] * float(
                            balances[balance])
                        x = "{:.2f}".format(x)
                        dict[balance.upper()] = x
                        total_balance = total_balance + float(x)

            percentage_change = "{:.2f}".format(
                (total_balance - 100000) / 1000)

    if request.method == "POST":
        #  check to see if available balance covers trade
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})
        currency_sold = request.form.get("currency_sold").lower()
        currency_bought = request.form.get("currency_bought").lower()
        if currency_sold.lower() == "usd":
            available_balance = balances[currency_sold]
        else:
            for coin in coins:
                if coin['symbol'] == currency_sold.upper():
                    sold_price = "{:.2f}".format(coin['quote']['USD']['price'])

            available_balance = balances[currency_sold] * int(
                float(sold_price))

        requested_balance = request.form.get("sold_amount")

        if int(requested_balance) > int(available_balance):
            flash(f"Insufficient funds - {currency_sold.upper()}")
            return render_template(
                "trade.html", selected_ticker=ticker, currencies=currencies,
                balances=balances, coins=coins)

        if currency_sold.upper() == currency_bought.upper():
            flash("Traded currencies must be different")
            return render_template(
                "trade.html", selected_ticker=ticker, currencies=currencies,
                balances=balances, coins=coins)

        # credit: stackoverflow.com how to get current date and time in python
        time_stamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        # code to get current prices for sold and bought currencies
        sold_price = 0
        bought_price = 0
        for coin in coins:
            if request.form.get("currency_sold").upper() == "USD":
                sold_price = 1
            elif coin['symbol'] == request.form.get("currency_sold").upper():
                sold_price = "{:.10f}".format(coin['quote']['USD']['price'])
                # sold_price = coin['quote']['USD']['price']
            if request.form.get("currency_bought").upper() == "USD":
                bought_price = 1
            elif coin['symbol'] == request.form.get("currency_bought"):
                bought_price = "{:.10f}".format(coin['quote']['USD']['price'])
                # bought_price = coin['quote']['USD']['price']

        # create the dictionary to be inserted into the db
        transaction = {
            "email": session["user"],
            "time_stamp": time_stamp,
            "currency_sold": request.form.get("currency_sold"),
            "sold_amount": float(request.form.get("sold_amount")),
            "sold_price": sold_price,
            "currency_bought": request.form.get("currency_bought"),
            "bought_price": float(bought_price),
        }
        mongo.db.transactions.insert_one(transaction)

        # update balances of cryptos sold and bought in balances document in db
        current_sold_balance = 0
        new_sold_balance = 0
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})

        for balance in balances:
            if balance.upper() == request.form.get("currency_sold").upper():
                current_sold_balance = balances[balance]
            if balance.upper() == request.form.get("currency_bought").upper():
                current_bought_balance = balances[balance]

        new_sold_balance = float(current_sold_balance) - (float(
            request.form.get("sold_amount")) / float(sold_price))
        new_bought_balance = float(current_bought_balance) + (
            float(request.form.get("sold_amount")) / float(bought_price))

        mongo.db.balances.update(
            {"email": session["user"]},
            {"$set":
                {
                    request.form.get(
                        "currency_sold").lower(): new_sold_balance,
                    request.form.get(
                        "currency_bought").lower(): new_bought_balance
                }
             }
        )

        flash("Trade Successfully Processed ")
        return redirect(url_for("portfolio"))

    return render_template(
        "trade.html", selected_ticker=ticker, currencies=currencies,
        balances=balances, coins=coins, dict=dict)


@app.route("/logout")
def logout():
    # delete user from session cookies
    flash("Log out successful")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    # change debug to False before submitting
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
