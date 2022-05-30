"""
Module containing the 'MySQL' Class.
"""

import mysql.connector as mysql

from typing import Any

from config import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD
from src.Interfaces.MVC.Model.database_interface import Database


class MySQL(Database):
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
        try:
            self.connection = mysql.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USERNAME,
                password=DB_PASSWORD
            )

            self.cursor = self.connection.cursor()

        except Exception as e:
            print('ERROR!')
            print(f'Error encountered while trying to connect to the DB. Traceback: {e}')
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
        try:
            self.cursor.close()
            self.connection.close()

        except Exception as e:
            print('ERROR!')
            print(f'Error encountered while trying to close the DB connection. Traceback: {e}')
            return False

        return True

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
