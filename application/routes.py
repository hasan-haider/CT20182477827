from application import app
from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html', login='executive')
    # edit login='val' to see navbar change val in ['False','cashier','executive']


# customer form added with regex
# frontend completed for create customer
@app.route('/create-customer')
def create_customer():
    return render_template('executive/customer/create.html', login='executive')


# account form added with regex
# frontend completed for create account
@app.route('/create-account')
def create_account():
    return render_template('executive/account/create.html', login='executive')
