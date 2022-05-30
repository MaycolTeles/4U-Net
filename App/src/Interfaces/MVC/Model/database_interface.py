"""
Module containing the 'Database' Interface.
"""

from flask import Flask

from typing import Protocol


class Database(Protocol):
    """
    Interface to represent a Database.

    This Interface contains all the 'Database' functionalities, like:
    
    - Handling database queries.

    This is an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    _instances = {}

    def __call__(cls, *args, **kwargs) -> Protocol:
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def connect(self, app: Flask) -> bool:
        """
        Method to connect to the database.

        This method must be implemented in all classes that
        implements this interface.

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

    def close(self) -> bool:
        """
        Method to close the connection to the database.

        This method must be implemented in all classes that
        implements this interface

        Returns
        --------
        bool
            - True if connection was successfully closed;
            - False otherwise.
        """
