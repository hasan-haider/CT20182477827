from flask import render_template, Blueprint, request, redirect, url_for, abort, flash
from flask_login import login_required

from application.models import customerAccount

cashier = Blueprint('cashier', __name__)
login = 0


@cashier.route('/accounts-operation')
@login_required
def account_detail():
    return render_template('cashier/account_detail.html', login=login)


'''
@cashier.route('/deposit-money')
@login_required
def deposit():
    #cust = customerAccount.query.filter_by(id=cust_data).first()
    return render_template('cashier/deposit.html', login=login, cust='')


'''
@cashier.route('/deposit-money-<cust_data>',methods=['GET','POST'])
@login_required
def deposit(cust_data):
    cust = customerAccount.query.filter_by(id=cust_data).first()
    return render_template('cashier/deposit.html', login=login, cust=cust)

@cashier.route('/transfer-money')
@login_required
def transfer():
    return render_template('cashier/transfer.html', login=login)


@cashier.route('/withdraw-money')
@login_required
def withdraw():
    return render_template('cashier/withdraw.html', login=login)


@cashier.route('/get-statements')
@login_required
def statements():
    return render_template('cashier/statements.html', login=login)
