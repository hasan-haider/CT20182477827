from flask import render_template, Blueprint, request, redirect, url_for, abort, flash, session
from flask_login import current_user

unauth_routes = Blueprint('routes', __name__)


# when user is authenticated
@unauth_routes.route('/')
def index():
    if current_user.is_authenticated:
        u_type = ''
        if session:
            u_type = session['u_type']
        return render_template('index.html', login=u_type)
    else:
        return redirect(url_for('routes.login'))

    # edit login='val' to see navbar change val in ['False','cashier','executive']


@unauth_routes.route('/login')
def login():
    return render_template('auth/login.html')


@unauth_routes.route('/register')
def register():
    return render_template('auth/register.html')
