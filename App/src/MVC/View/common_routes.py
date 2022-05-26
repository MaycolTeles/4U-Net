"""
Module containing the 'CommonRoutes'.
"""

from flask import Flask, render_template

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


    def index(self) -> str:
        """
        Method to render the index page.

        Returns
        --------
        str:
            The index page rendered in str format.
        """
        return render_template('index.html')
