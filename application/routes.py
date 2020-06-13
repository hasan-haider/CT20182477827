from flask import render_template, Blueprint, request, redirect, url_for, abort, flash

unauth_routes = Blueprint('routes', __name__)


@unauth_routes.route('/')
def index():
    return render_template('index.html', login='executive')
    # edit login='val' to see navbar change val in ['False','cashier','executive']


@unauth_routes.route('/login')
def login():
    return render_template('auth/login.html', login='False')
