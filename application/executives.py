from flask import render_template, Blueprint, request, redirect, url_for, abort, flash
from flask_login import current_user, login_required
from markupsafe import Markup

from .models import customerAccount
from . import db

executives = Blueprint('executives', __name__)


# customer form added with regex
# frontend completed for create customer
@executives.route('/create-customer')
@login_required
def create_customer():
    if current_user.is_executive():
        return render_template('executive/customer/create.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/update-customer', methods=['GET', 'POST'])
@login_required
def update_customer():
    if current_user.is_executive():
        return render_template('executive/customer/update.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/delete-customer')
@login_required
def delete_customer():
    if current_user.is_executive():
        return render_template('executive/customer/delete.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/customer-status')
@login_required
def customer_status():
    if current_user.is_executive():
        return render_template('executive/customer/status.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/search-customer', methods=['GET', 'POST'])
@login_required
def search_customer():
    if current_user.is_executive():
        # dummy()
        cid = request.form.get('search_cust_id')
        aid = request.form.get('search_acc_id')
        cust = None
        if cid:
            cust = customerAccount.query.filter_by(id=cid).first()
        elif aid:
            cust = customerAccount.query.filter_by(aid=aid).first()
        if cust:
            print(cust.status)
            return render_template('cashier/account_detail.html', cust=cust)

        return render_template('cashier/account_detail.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/customer-profile')
@login_required
def customer_profile():
    if current_user.is_executive():
        return render_template('executive/customer/customer_detail.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


# account form added with regex
# frontend completed for create account
@executives.route('/create-account')
@login_required
def create_account():
    if current_user.is_executive():
        return render_template('executive/account/create.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/delete-account')
@login_required
def delete_account():
    if current_user.is_executive():
        return render_template('executive/account/delete.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/account-status')
@login_required
def account_status():
    if current_user.is_executive():
        return render_template('executive/account/status.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


@executives.route('/search-account')
@login_required
def search_account():
    if current_user.is_executive():
        return render_template('executive/account/search.html')
    else:
        message = Markup("Error: Not authenticated to perform action.<br /> Contact Administrator if this is a mistake")
        flash(message, 'danger')
        return redirect(url_for('routes.index'))


def dummy():
    customer = customerAccount(id=1, ssn=987654321, aid=123789456, atpye=0, status='Active', msg=None)
    db.session.add(customer)
    db.session.commit()
