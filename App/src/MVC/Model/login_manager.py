"""
Module containing the 'LoginManager' Class.
"""

from flask import Flask
from flask_login import LoginManager as LoginManagerClass, UserMixin

from App.src.Entities.SQLAlchemy.user import User
from App.src.Interfaces.MVC.Model.database_interface import Database


class LoginManager(LoginManagerClass, Database):
    """
    Class to represent the LoginManager.

    This class implements the 'Database' Interface,
    so it must implement all the 'Database' functionalities, like:
    
    - Handling database queries.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def connect(self, app: Flask) -> bool:
        """
        Method to connect to the LoginManager.

        Parameters
        -----------
        app : Flask
            The Flask application to initialize the LoginManager.

        Returns
        --------
        bool
            - True if connection was successfully established;
            - False otherwise.
        """
        try:
            self.init_app(app)

        except Exception as e:
            print('ERROR!')
            print(f'Error while trying to create a LoginManager. Error: {e}')
            return False

        return True

    def close(self) -> bool:
        """
        Method to close the LOginManager connection.

        Returns
        --------
        bool
            - True if connection was successfully closed;
            - False otherwise.
        """    


login_manager = LoginManager()


@login_manager.user_loader
def load_user() -> UserMixin:
        """
        Method to load the user

        Parameters
        -----------
        id : str
            The user id.

        Returns
        -----------
        UserMixin:
            The current user.
        """
        return User.query.get(int(id))
