from flask_login import UserMixin

from application import db
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    userId = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    # 0 - cashier/teller, 1- customer executives
    aadhar = db.Column(db.String(50), nullable=False)
    timeStamp = db.Column(db.DateTime, default=datetime.now)


class customerAccount(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement = True)
    ssn = db.Column(db.Integer, nullable = False)
    aid = db.Column(db.Integer, nullable = False)
    atpye = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String(10), nullable = False)
    msg = db.Column(db.String(500))
    lastUpdated = db.Column(db.DateTime, default = datetime.now)


#usr = User.query.filter_by(password="123456")
#print(usr.userId, usr.password)