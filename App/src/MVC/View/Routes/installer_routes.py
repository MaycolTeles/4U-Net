"""
Module containing the 'InstallerRoutes' Class.
"""

from flask import Flask, render_template


from App.src.Entities.API.ViasatAPI.installers_api import APIInstallers

from App.src.Interfaces.MVC.View.route_interface import Route


class InstallerRoutes(Route):
    """
    Class containing all the Installer Routes.
    """

    def __init__(self, api: APIInstallers) -> None:
        """
        Constructor the create a reference to the Plans API.
        """
        self.api = api

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all the installer routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        app.add_url_rule('/instaladores', view_func=self.installers)
        app.add_url_rule('/instaladores/<installer_id>', view_func=self.installer)

    # ROUTES:
    def installers(self) -> str:
        """
        Method to render the page containing all installers.

        Returns
        --------
        str:
            The installers page rendered in str format.
        """
        installers = self.api.get_installers()

        return render_template(
            'Installers/installers.html',
            installers=installers,
            len_installers=len(installers)
        )

    def installer(self, installer_id: str) -> str:
        """
        Method to render the page containing a single installer,
        which the id was received as argument.

        Parameters
        ----------
        installer_id : str
            The installer id

        Returns
        --------
        str:
            The installers page rendered in str format.
        """
        installer = self.api.get_installers_from_installer_id(installer_id)

        return render_template('Installers/installer.html', installer=installer)
