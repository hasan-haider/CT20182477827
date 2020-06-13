from flask import render_template, Blueprint, request, redirect, url_for, abort, flash

cashier = Blueprint('cashier', __name__)
