from flask import render_template, Blueprint, request, redirect, url_for, abort, flash
from flask_login import current_user, login_required

executives = Blueprint('executives', __name__)
login = 1

# customer form added with regex
# frontend completed for create customer
@executives.route('/create-customer')
@login_required
def create_customer():
    return render_template('executive/customer/create.html', login=login)


@executives.route('/update-customer')
@login_required
def update_customer():
    return render_template('executive/customer/update.html', login=login)


@executives.route('/delete-customer')
@login_required
def delete_customer():
    return render_template('executive/customer/delete.html', login=login)


@executives.route('/customer-status')
@login_required
def customer_status():
    return render_template('executive/customer/status.html', login=login)


@executives.route('/search-customer')
@login_required
def search_customer():
    return render_template('executive/customer/search.html', login=login)


@executives.route('/customer-profile')
@login_required
def customer_profile():
    return render_template('executive/customer/customer_detail.html', login=login)


# account form added with regex
# frontend completed for create account
@executives.route('/create-account')
@login_required
def create_account():
    return render_template('executive/account/create.html', login=login)


@executives.route('/delete-account')
@login_required
def delete_account():
    return render_template('executive/account/delete.html', login=login)


@executives.route('/account-status')
@login_required
def account_status():
    return render_template('executive/account/status.html', login=login)


@executives.route('/search-account')
@login_required
def search_account():
    return render_template('executive/account/search.html', login=login)
