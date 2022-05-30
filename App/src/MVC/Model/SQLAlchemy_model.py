"""
Module containing the 'MySQL' Class.
"""

from flask import Flask
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from os import path

from App.config import DB_NAME


class SQLAlchemyModel(SQLAlchemy):
    """
    Class to represent the SQLAlchemy Database.

    This class implements the 'Database' Interface,
    so it must implement all the 'Database' functionalities, like:
    
    - Handling database queries.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def connect(self, app: Flask) -> bool:
        """
        Method to connect to the database.

        Parameters
        -----------
        app : Flask
            The Flask application to initialize the DB.

        Returns
        --------
        bool
            - True if connection was successfully established;
            - False otherwise.
        """
        try:
            self.init_app(app)
            # TODO: CHECK IF THIS WORKS
            # self.create_database(app)

        except Exception as e:
            print('ERROR!')
            print(f'Error while trying to connect into the SQLAlchemy. Error: {e}')
            return False

        return True

    def create_database(self, app: Flask):
        """
        Method to create the database if it doesn't exists yet.

        Parameters
        -----------
        app : Flask
            The Flask app.
        """
        if not path.exists('App/src/' + DB_NAME):
            database.create_all(app=app)
            print("Database created!")
    
    def add_user(self, username: str, email: str, password: str) -> bool:
        """
        Method to add a new user to the database.

        Parameters
        -----------
        ...

        Returns
        --------
        bool
            - True if user was successfully added;
            - False otherwise.
        """
        try:
            from App.src.Entities.SQLAlchemy.user import User
            new_user = User(
                username=username,
                email=email,
                password=generate_password_hash(password, method='sha256')
            )

            self.session.add(new_user)
            self.session.commit()

        except Exception as e:
            print('ERROR!')
            print(
                'Error while trying to add a new user to the database.'
                f'Error: {e}'
            )
            return False

        else:
            login_user(new_user, remember=True)

        return True


database = SQLAlchemyModel()
