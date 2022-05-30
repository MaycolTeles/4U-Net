"""
Module containing all routes that are common for all users.
"""

from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import logout_user, login_required

from App.config import HTTP_METHODS
from App.src.MVC.Controller.controller import controller


common_routes = Blueprint('common_routes', __name__)


# ROUTES:
@common_routes.route('/')
@common_routes.route('/home')
@common_routes.route('/index')
def index() -> str:
    """
    Function to create the '/', '/home' and '/index' routes and
    render the index page.

    Returns
    --------
    str:
        The index page rendered in str format.
    """
    return render_template("Common/index.html")


@common_routes.route('/registrar', methods=HTTP_METHODS)
def register() -> str:
    """
    Function to render the registration page.

    Returns
    --------
    str:
        The registration page rendered in str format.
    """
    if request.method == 'POST':
        controller.handle_register_post()

    return render_template("Common/register.html")


@common_routes.route('/login', methods=HTTP_METHODS)
def login() -> str:
    """
    Function to render the login page.

    Returns
    --------
    str:
        The login page rendered in str format.
    """
    if request.method == 'POST':
        controller.handle_login_post()

    return render_template("Common/login.html")


@common_routes.route('/logout')
@login_required
def logout() -> str:
    """
    Function to render the logout page.

    Returns
    --------
    str:
        The logout page rendered in str format.
    """
    logout_user()
    return redirect(url_for('index'))
