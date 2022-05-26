"""
Module containing the "Routes" Class.
"""

from flask import Flask

from src.Interfaces.MVC.View.route_interface import Route

from src.MVC.View.common_routes import CommonRoutes
from src.MVC.View.client_routes import ClientRoutes
from src.MVC.View.installer_routes import InstallerRoutes


class Routes(Route):
    """
    Class containing all the routes
    """

    entities = [
        CommonRoutes(),
        ClientRoutes(),
        InstallerRoutes()
    ]

    def create_routes(self, app: Flask):
        """
        Method to create all the routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        
        for entity in self.entities:
            entity.create_routes(app)
