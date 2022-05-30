"""
Module containing all the needed instantiations. 
"""

from App.src.app import FlaskApp

from App.src.MVC.Model.SQLAlchemy_model import database
from App.src.MVC.Model.login_manager_model import login_manager
from App.src.MVC.View.Routes.routes import routes


def create_app():
    """
    Function to create a Flask app.

    Returns
    --------
    FlaskApp:
        The Flask app.
    """

    flask_app = FlaskApp(database, login_manager, routes)

    return flask_app
