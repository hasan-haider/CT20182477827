from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST'])
# authentication for signup/registration page
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    # db.session.add(usr)
    # db.session.commit()
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


# authentication for login page
@auth.route('/login-post', methods=['GET','POST'])
def login_post():
    if request.method == 'POST':
        print(request.form.get( 'uname'))
        email = request.form.get('uname')
        password = request.form.get('inputPassword')
        # remember = True if request.form.get('remember') else False
        print("Hi Iam performing auth")
        print(email, password)
        #usr = User(userId=email, password=password, type=0)
        # db.session.add(usr)
        # db.session.commit()
        # add the new user to the database
        #db.session.add(usr)
        #db.session.commit()
        user = User.query.filter_by(userId=email).first()
        #print(user.userId)
        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if(email == user.userId and password == user.password):
            return redirect(url_for('routes.index'))


    flash('Please check your login details and try again.')

            # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        #login_user(user)  # ,remember=remember)
         # address of profile or main page
    return redirect(url_for('routes.login'))

# if a user tries to access page without loggin in
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))  # address of index page
