"""
Module containing the 'MyDatabase' Class.
"""

from typing import Any

from App.src.Interfaces.MVC.Model.database_interface import Database


class MyDatabase(Database):
    """
    Class to represent a generic Database.

    This class implements the 'Database' Interface,
    so it must implement all the 'Database' functionalities, like:
    
    - Handling database queries.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def connect(self) -> bool:
        """
        Method to connect to the database.

        Returns
        --------
        bool
            - True if connection was successfully established;
            - False otherwise.
        """
        ...

    def close(self) -> bool:
        """
        Method to close the connection to the database.

        Returns
        --------
        bool
            - True if connection was successfully closed;
            - False otherwise.
        """
        ...

    def insert_data(self, data: Any) -> bool:
        """
        Method to insert some data into the database.

        Returns
        --------
        bool
            - True if data was successfully inserted into the database;
            - False otherwise.
        """
        ...

    def read_data(self) -> Any:
        """
        Method to read some data from the database.

        Returns
        --------
        Any
            The data that was read.
        """
        ...

    def update_data(self, data: Any) -> bool:
        """
        Method to update some data in the database.

        Parameters
        -----------
        data : Any
            The data to be updated in the database.

        Returns
        --------
        bool
            - True if data was successfully updated;
            - False otherwise.
        """
        ...

    def delete_data(self, data: Any) -> bool:
        """
        Method to delete some data from the database.

        Parameters
        -----------
        data : Any
            The data to be deleted in the database.

        Returns
        --------
        bool
            - True if data was successfully deleted;
            - False otherwise.
        """
        ...
