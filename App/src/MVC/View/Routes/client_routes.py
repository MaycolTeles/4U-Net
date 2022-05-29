"""
Module containing the 'ClientRoutes' Class.
"""

from flask import Flask, render_template

from App.src.Interfaces.MVC.View.route_interface import Route


class ClientRoutes(Route):
    """
    Class containing all the Client Routes.
    """

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all the client routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        app.add_url_rule('/clientes', view_func=self.clients)
        app.add_url_rule('/clientes/<client_name>', view_func=self.client)

    # ROUTES:
    def clients(self) -> str:
        """
        Method to render the clients page.

        Returns
        --------
        str:
            The clients page rendered in str format.
        """
        return render_template('Clients/clients.html')

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
        return render_template('Clients/clients.html', client_name=client_name)
