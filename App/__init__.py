"""
Module containing all the needed instantiations. 
"""

from flask import Flask

from os import path

from App.config import DB_NAME

from App.src.app import App
from App.src.MVC.Model.SQLAlchemy import database
from App.src.MVC.Model.login_manager import login_manager
from App.src.MVC.View.Routes.routes import routes

from App.src.Entities.SQLAlchemy.user import User


def create_app() -> Flask:
    """
    Function to create a Flask app.

    Returns
    --------
    Flask:
        The Flask app.
    """

    flask = App(database, login_manager, routes)

    database.connect(flask.app)
    login_manager.connect(flask.app)

    create_database(flask.app)

    return flask

def create_database(app):
    if not path.exists("SQLAlchemy/" + DB_NAME):
        database.create_all(app=app)
        print("Database created!")
