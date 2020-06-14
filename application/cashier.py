from flask import render_template, Blueprint, request, redirect, url_for, abort, flash
from flask_login import login_required

cashier = Blueprint('cashier', __name__)
login = 0


@cashier.route('/accounts-operation')
@login_required
def account_detail():
    return render_template('cashier/account_detail.html', login=login)


@cashier.route('/deposit-money')
@login_required
def deposit():
    return render_template('cashier/deposit.html', login=login)


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
