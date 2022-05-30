"""
Module containing all routes related to the clients.
"""

from flask import Blueprint, render_template


client_routes = Blueprint('client_routes', __name__)


# ROUTES:
@client_routes.route('/clientes')
def clients() -> str:
    """
    Function to create the '/clientes' route and
    render the clients page.

    Returns
    --------
    str:
        The clients page rendered in str format.
    """
    return render_template('Clients/clients.html')


@client_routes.route('/cliente')
def client(client_name: str) -> str:
    """
    Function to create the '/cliente' rounte and
    render the client page, based on a single client.

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
