from flask import render_template, Blueprint, request, redirect, url_for, abort, flash

executives = Blueprint('executives', __name__)


# customer form added with regex
# frontend completed for create customer
@executives.route('/create-customer')
def create_customer():
    return render_template('executive/customer/create.html', login='executive')


@executives.route('/update-customer')
def update_customer():
    return render_template('executive/customer/update.html', login='executive')


@executives.route('/delete-customer')
def delete_customer():
    return render_template('executive/customer/delete.html', login='executive')


@executives.route('/customer-status')
def customer_status():
    return render_template('executive/customer/status.html', login='executive')


# account form added with regex
# frontend completed for create account
@executives.route('/create-account')
def create_account():
    return render_template('executive/account/create.html', login='executive')


@executives.route('/delete-account')
def delete_account():
    return render_template('executive/account/delete.html', login='executive')
