"""
Module containing the 'CommonRoutes' Class.
"""

from flask import Flask, redirect, render_template, url_for, request

from App.config import HTTP_METHODS

from App.src.Interfaces.MVC.View.route_interface import Route


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
        app.add_url_rule('/logout', methods=HTTP_METHODS, view_func=self.logout)

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
            # TODO: IMPLEMENT THE LOGIN LOGIC
            redirect(url_for('index'))

        return render_template("Common/login.html")

    def logout(self) -> str:
        """
        Method to render the logout page.

        Returns
        --------
        str:
            The logout page rendered in str format.
        """
        # TODO: IMPLEMENT THE LOGOUT LOGIC
        return redirect(url_for('login'))

    def page_not_found(self, error) -> str:
        """
        Method to render a generic error page (404).

        Returns
        --------
        str:
            The error page rendered in str format.
        """
        return render_template("Common/error_404.html")
