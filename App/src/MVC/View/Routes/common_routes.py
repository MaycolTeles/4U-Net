"""
Module containing the 'CommonRoutes' Class.
"""

from flask import Flask, redirect, render_template, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from App.config import HTTP_METHODS

from App.src.Entities.SQLAlchemy.user import User
from App.src.Interfaces.MVC.View.route_interface import Route

from App.src.Exceptions.user_not_found_exception import UserNotFoundException


class CommonRoutes(Route):
    """
    Class containing all the routes that are common for everyone.
    """

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all the common routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        app.add_url_rule('/', view_func=self.index)
        app.add_url_rule('/index', view_func=self.index)
        app.add_url_rule('/home', view_func=self.index)

        app.add_url_rule('/register', methods=HTTP_METHODS, view_func=self.register)
        app.add_url_rule('/login', methods=HTTP_METHODS, view_func=self.login)
        app.add_url_rule('/logout', view_func=self.logout)

        app.register_error_handler(404, self.page_not_found)

    # ROUTES:
    def index(self) -> str:
        """
        Method to render the index page.

        Returns
        --------
        str:
            The index page rendered in str format.
        """
        return render_template("Common/index.html")

    def register(self) -> str:
        """
        Method to render the registration page.

        Returns
        --------
        str:
            The registration page rendered in str format.
        """
        if request.method == 'POST':
            # TODO: IMPLEMENT THE REGISTER LOGIC
            redirect(url_for('index'))

        return render_template("Common/register.html")

    def login(self) -> str:
        """
        Method to render the login page.

        Returns
        --------
        str:
            The login page rendered in str format.
        """
        if request.method == 'POST':
            self.__handle_login_post()

        return render_template("Common/login.html")

    def __handle_login_post(self) -> None:
        """
        Method to handle the 'POST' http method at the 'login' page.
        """
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            raise UserNotFoundException

        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('index'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    @login_required
    def logout(self) -> str:
        """
        Method to render the logout page.

        Returns
        --------
        str:
            The logout page rendered in str format.
        """
        logout_user()
        return redirect(url_for('index'))

    def page_not_found(self, error) -> str:
        """
        Method to render a generic error page (404).

        Returns
        --------
        str:
            The error page rendered in str format.
        """
        return render_template("Common/error_404.html")
