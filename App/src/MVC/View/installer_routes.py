"""
Module containing the 'InstallerRoutes'.
"""

from flask import Flask, render_template

from src.Interfaces.MVC.View.route_interface import Route


class InstallerRoutes(Route):
    """
    Class containing all the Installer Routes.
    """

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all the common routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        app.add_url_rule('/instaladores/', view_func=self.installers)
        app.add_url_rule('/instaladores/<installer_name>', view_func=self.installer)

    # ROUTES:
    def installers(self) -> str:
        """
        Method to render the installer page.

        Returns
        --------
        str:
            The installers page rendered in str format.
        """
        return render_template('installers.html')

    def installer(self, installer_name: str) -> str:
        """
        Method to render the installer page, based on a single installer.

        Parameters
        ----------
        installer_name : str
            The installer name

        Returns
        --------
        str:
            The installers page rendered in str format.
        """
        return render_template('installers.html', installer_name=installer_name)
