"""
Module containing the 'ClientRoutes'.
"""

from flask import Flask, render_template

from src.Interfaces.MVC.View.route_interface import Route


class ClientRoutes(Route):
    """
    Class containing all the Client Routes.
    """

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all the common routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        app.add_url_rule('/clients', view_func=self.clients)
        app.add_url_rule('/cliente/<client_name>', view_func=self.client)

    # ROUTES:
    def clients(self) -> str:
        """
        Method to render the clients page.

        Returns
        --------
        str:
            The clients page rendered in str format.
        """
        return render_template('clients.html')

    def client(self, client_name: str) -> str:
        """
        Method to render the client page, based on a single client.

        Parameters
        ----------
        client_name : str
            The client name

        Returns
        --------
        str:
            The clients page rendered in str format.
        """
        return render_template('clients.html', client_name=client_name)
