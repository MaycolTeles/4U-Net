"""
Module containing the 'CommonRoutes' Class.
"""

from flask import Flask, render_template


from typing import Tuple


from src.Interfaces.MVC.View.route_interface import Route


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

    def page_not_found(self, error) -> str:
        """
        Method to render a generic error page (404).

        Returns
        --------
        str:
            The error page rendered in str format.
        """
        return render_template("Common/error_404.html")
