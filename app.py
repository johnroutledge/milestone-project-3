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

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_currencies")
def get_currencies():
    currencies = mongo.db.currencies.find()

    # code to get cryptocurrency prices adapted from Coding Under Pressure YouTube channel
    # 'How to Use an API in Python to get Bitcoin's Price Live - Along with other Cryptocurrencies'
    headers = {
        'X-CMC_PRO_API_KEY' : coin_market_cap_key,
        'Accepts' : 'application/json'
    }

    params = {
        'start' : '1',
        'limit' : '20',
        'convert' : 'USD'
    }

    try:
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        json = requests.get(url, params=params, headers=headers).json()
        coins = json['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        flash(e)

    return render_template("currencies.html", currencies = currencies, coins = coins)


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        # check if email already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("email already registered")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").capitalize(),
            "last_name": request.form.get("last_name").capitalize(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password").lower())
        }

        balances = {
            "email": request.form.get("email").lower(),
            "USD": 100000,
            "BTC": 0,
            "ETH": 0,
            "DOGE": 0,
            "ADA": 0,
            "LTS": 0,
            "SOL": 0,
            "USDT": 0
        }
        mongo.db.users.insert_one(register)
        mongo.db.balances.insert_one(balances)

        # put the new user into session cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful")
        return redirect(url_for("portfolio", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods = ["GET", "POST"])
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
                    return redirect(url_for(
                        "portfolio", username=session["user"]))
            else:
                # incorrect password
                flash("Incorrect email and/or password")
                return redirect(url_for("login"))

        else:
            # email doesn't exist
            flash("Incorrect email and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/portfolio/", methods=["GET", "POST"])
def portfolio():
    if "user" not in session:
        return redirect(url_for("login"))

    # get users first name from db
    username = mongo.db.users.find_one(
        {"email": session["user"]})["first_name"]
    
    if session["user"]:
        # retrieve user's balance for each cryptocurrency
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})

        # retrieve all tradable cryptocurrencies
        currencies = mongo.db.currencies.find()

        # code to get cryptocurrency prices adapted from Coding Under Pressure YouTube channel
        # 'How to Use an API in Python to get Bitcoin's Price Live - Along with other Cryptocurrencies'
        headers = {
            'X-CMC_PRO_API_KEY' : coin_market_cap_key,
            'Accepts' : 'application/json'
        }

        params = {
            'start' : '1',
            'limit' : '20',
            'convert' : 'USD'
        }

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        json = requests.get(url, params=params, headers=headers).json()
        coins = json['data']

        # create a dictionary which calculate the user's balance for each cryptocurrency
        dict = {}
        totalBalance = 0
        for balance in balances:
            if balance.upper() == "USD":
                x = balances[balance]
                dict[balance.upper()] = x
                totalBalance = totalBalance + float(x)
            else:
                for coin in coins:
                    if coin['symbol'] == balance.upper():    
                        x = coin['quote']['USD']['price'] * balances[balance]
                        x = "{:.2f}".format(x)
                        dict[balance.upper()] = x
                        totalBalance = totalBalance + float(x)

            totalBalance = float(totalBalance)

        return render_template(
            "portfolio.html", username=username, currencies=currencies, balances=balances, coins=coins, dict=dict, totalBalance=totalBalance)

    return redirect(url_for("login"))


@app.route("/trade/<ticker>", methods=["GET", "POST"])
def trade(ticker):
    if session["user"]:
        # retrieve user's balance for each cryptocurrency
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})

        # retrieve all tradable cryptocurrencies
        currencies = mongo.db.currencies.find()

        # code to get cryptocurrency prices adapted from Coding Under Pressure YouTube channel
        # 'How to Use an API in Python to get Bitcoin's Price Live - Along with other Cryptocurrencies'
        headers = {
            'X-CMC_PRO_API_KEY' : coin_market_cap_key,
            'Accepts' : 'application/json'
        }

        params = {
            'start' : '1',
            'limit' : '20',
            'convert' : 'USD'
        }

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        json = requests.get(url, params=params, headers=headers).json()
        coins = json['data']

    if request.method == "POST":
        #  check to see if available balance covers trade
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})
        currency_sold = request.form.get("currency_sold")
        available_balance = balances[currency_sold]
        requested_balance = request.form.get("sold_amount")

        if int(requested_balance) > int(available_balance):
            flash("Insufficient funds")
            return render_template(
                "trade.html", selected_ticker=ticker, currencies=currencies, balances=balances, coins=coins)

        # credit: stackoverflow.com how to get current date and time in python
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # code to get current prices for sold and bought currencies
        sold_price = 0
        bought_price = 0
        for coin in coins:
            if request.form.get("currency_sold").upper() == "USD":
                sold_price = 1
            elif coin['symbol'] == request.form.get("currency_sold"):
                sold_price = "{:.2f}".format(coin['quote']['USD']['price'])
            if coin['symbol'] == request.form.get("currency_bought"):
                bought_price = "{:.2f}".format(coin['quote']['USD']['price'])

        # create the dictionary to be inserted into the db
        transaction = {
            "email": session["user"],
            "time_stamp": time_stamp,
            "currency_sold": request.form.get("currency_sold"),
            "sold_amount": request.form.get("sold_amount"),
            "sold_price": sold_price,
            "currency_bought": request.form.get("currency_bought"),
            "bought_price": bought_price,
        }
        mongo.db.transactions.insert_one(transaction)
        
        # update balances document in DB
        current_sold_balance = 0
        new_sold_balance = 0

        balances = mongo.db.balances.find_one(
            {"email": session["user"]})

        for balance in balances:
            if balance.upper() == request.form.get("currency_sold").upper():
                current_sold_balance = balances[balance]
            if balance.upper() == request.form.get("currency_bought").upper():
                current_bought_balance = balances[balance]

        new_sold_balance = int(current_sold_balance) - int(request.form.get("sold_amount"))

        mongo.db.balances.update(
            { "email": session["user"] },
            { "$set":
                {request.form.get("currency_sold"): new_sold_balance }
            }
        )

        flash("Trade Successfully Processed ")
        return redirect(url_for("portfolio"))

    return render_template(
        "trade.html", selected_ticker=ticker, currencies=currencies, balances=balances, coins=coins)


@app.route("/logout")
def logout():
    # delete user from session cookies
    flash("Log out successful")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)  #change to False before submitting