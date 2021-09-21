import os
import requests
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MOGNO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
coin_market_cap_key = os.environ.get("COIN_MARKET_CAP_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
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

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    json = requests.get(url, params=params, headers=headers).json()
    coins = json['data']

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
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password").lower())
        }
        mongo.db.users.insert_one(register)

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


@app.route("/portfolio/<username>", methods=["GET", "POST"])
def portfolio(username):
    # get users first name from db
    username = mongo.db.users.find_one(
        {"email": session["user"]})["first_name"]
    
    if session["user"]:
        # calculate portfolio balance
        balances = mongo.db.balances.find_one(
            {"email": session["user"]})

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
        for balance in balances:
            for coin in coins:
                if coin['symbol'] == balance.upper():    
                    # x = "{:.2f}".format(coin['quote']['USD']['price']) * balances[balance]
                    x = coin['quote']['USD']['price'] * balances[balance]
                    x = "{:.2f}".format(x)
                    dict[balance.upper()] = x
                elif balance.upper() == "USD":
                    x = balances[balance]
                    dict[balance.upper()] = x
                

        return render_template(
            "portfolio.html", username=username, currencies=currencies, balances=balances, coins=coins, dict=dict)

    return redirect(url_for("login"))


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