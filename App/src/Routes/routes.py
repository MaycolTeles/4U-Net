"""
Module containing all the App Routes.
"""

from flask import render_template

from src.Routes.client_routes import ClientRoutes
from src.Routes.installer_routes import InstallerRoutes


class Routes():
    """
    Class containing all the App Routes.
    """

    clientRoutes: ClientRoutes
    installerRoutes: InstallerRoutes

    @staticmethod
    def index() -> str:
        """
        Method to render the index page.

        Returns
        --------
        str:
            The html page rendered in str format.
        """
        return render_template('index.html')
