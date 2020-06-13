from flask import Blueprint,render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/index')
def index():
    return render_template('index.html')

#html page for profile or first page
'''@main.route('/profile')
def profile():
    return render_template('profile.html')'''
