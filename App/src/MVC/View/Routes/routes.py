"""
Module containing the "Routes" Class.
"""

from flask import Flask

from App.src.MVC.View.Routes.error_routes import error_routes
from App.src.MVC.View.Routes.common_routes import common_routes
from App.src.MVC.View.Routes.client_routes import client_routes
from App.src.MVC.View.Routes.installer_routes import installers_routes
from App.src.MVC.View.Routes.plans_routes import plans_routes


class Routes():
    """
    Class to register all the blueprints routes.
    """

    blueprints = {
        error_routes: '',
        common_routes: '/',
        client_routes: '/clientes',
        installers_routes: '/instaladores',
        plans_routes: '/planos'
    }

    def register_blueprints(self, app: Flask):
        """
        Method to create all the routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """

        for blueprint, url in self.blueprints.items():
            app.register_blueprint(blueprint, url_prefix=url)


routes = Routes()
