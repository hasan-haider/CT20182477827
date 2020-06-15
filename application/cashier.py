from flask import render_template, Blueprint, request, redirect, url_for, abort, flash
from flask_login import login_required
from . import db

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

@cashier.route('/transfer-money-<cust_data>', methods = ['GET','POST'])
@login_required
def transfer(cust_data):
    cust = customerAccount.query.filter_by(id=cust_data).first()
    return render_template('cashier/transfer.html', login=login, cust = cust)


@cashier.route('/withdraw-money-<cust_data>', methods = ['GET','POST'])
@login_required
def withdraw(cust_data):
    cust = customerAccount.query.filter_by(id=cust_data).first()
    return render_template('cashier/withdraw.html', login=login, cust= cust)


@cashier.route('/get-statements')
@login_required
def statements():
    return render_template('cashier/statements.html', login=login)

@cashier.route('/deduct-<cust_data>', methods = ['GET', 'POST'])
@login_required
def deduct(cust_data):
    wamt = request.form.get('wamt')
    print(wamt)
    print(cust_data)
    cust = customerAccount.query.filter_by(id=cust_data).first()
    #cust.balance = 10000
    #db.session.commit()
    if int(cust.balance) >= int(wamt) and int(cust.balance) >0:
        cust.balance = int(cust.balance) - int(wamt)
        db.session.commit()
        return render_template('cashier/account_detail.html', login=login, cust = cust)

    return render_template('cashier/withdraw.html', login=login, cust = cust)

@cashier.route('/add-<cust_data>', methods = ['GET', 'POST'])
@login_required
def add(cust_data):
    wamt = request.form.get('wamt')
    print(wamt)
    print(cust_data)
    cust = customerAccount.query.filter_by(id=cust_data).first()
    #cust.balance = 10000
    #db.session.commit()

    cust.balance = int(cust.balance) + int(wamt)
    db.session.commit()
    return render_template('cashier/account_detail.html', login=login, cust = cust)

@cashier.route('/transfercust-<cust_data>', methods = ['GET', 'POST'])
@login_required
def transfercust(cust_data):
    wamt = request.form.get('wamt')
    tarid = request.form.get('tar_id')
    type = request.form.get('t_acc_type')
    cust = customerAccount.query.filter_by(id=cust_data).first()
    tar = customerAccount.query.filter_by(id=tarid).first()
    if tar.atpye== 0:
        ttype = "Savings"
    else:
        ttype = "Current"

    if  tar and int(cust.balance)>0 and int(cust.balance)>= int(wamt) and int(cust.id)!=int(tar.id) and type == ttype:
        cust.balance = int(cust.balance) - int(wamt)
        tar.balance = int(tar.balance) + int(wamt)
        db.session.commit()
        return render_template('cashier/account_detail.html', login=login, cust=cust)

    return render_template('cashier/transfer.html', login=login, cust = cust)