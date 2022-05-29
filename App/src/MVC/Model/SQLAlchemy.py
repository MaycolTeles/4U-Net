"""
Module containing the 'MySQL' Class.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyClass
from App.src.Entities.SQLAlchemy.user import User

from App.src.Interfaces.MVC.Model.database_interface import Database


class SQLAlchemy(SQLAlchemyClass, Database):
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

        except Exception as e:
            print('ERROR!')
            print(f'Error while trying to connect into the SQLAlchemy. Error: {e}')
            return False

        return True

    def close(self) -> bool:
        """
        Method to close the database connection.

        Returns
        --------
        bool
            - True if connection was successfully closed;
            - False otherwise.
        """
        return True
    
    def add_user(self, user: User) -> bool:
        """
        Method to add a new user to the database.

        Parameters
        -----------
        user : User
            The user to be added to the database.

        Returns
        --------
        bool
            - True if user was successfully added;
            - False otherwise.
        """
        try:
            database.session.add(user)
            database.session.commit()

        except Exception as e:
            print('ERROR!')
            print(
                'Error while trying to add a new user to the database.'
                f'Error: {e}'
            )
        

database = SQLAlchemy()
