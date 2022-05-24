"""
Module containing the 'ClientRoutes'.
"""

from flask import render_template


class ClientRoutes():
    """
    Class containing all the Client Routes.
    """

    @staticmethod
    def clients(client_name: str) -> str:
        """
        Method to render the client page.

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
