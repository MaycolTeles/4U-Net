"""
Module containing the "Routes" Class.
"""

from flask import Flask


from src.Entities.API.ViasatAPI.plans_api import APIPlans
from src.Entities.API.ViasatAPI.installers_api import APIInstallers

from src.Interfaces.MVC.View.route_interface import Route

from src.MVC.View.Routes.common_routes import CommonRoutes
from src.MVC.View.Routes.client_routes import ClientRoutes
from src.MVC.View.Routes.installer_routes import InstallerRoutes
from src.MVC.View.Routes.plans_routes import PlansRoutes


class Routes(Route):
    """
    Class containing all the routes
    """

    entities = [
        CommonRoutes(),
        ClientRoutes(),
        InstallerRoutes(APIInstallers()),
        PlansRoutes(APIPlans())
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
