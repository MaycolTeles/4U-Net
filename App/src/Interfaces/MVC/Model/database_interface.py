"""
Module containing the 'Database' Interface.
"""

from typing import Any, Protocol


class Database(Protocol):
    """
    Interface to represent a Database.

    This Interface contains all the 'Database' functionalities, like:
    
    - Handling database queries.

    This is an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def connect(self) -> bool:
        """
        Method to connect to the database.

        This method must be implemented in all classes that
        implements this interface.

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

        This method must be implemented in all classes that
        implements this interface

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

        This method must be implemented in all classes that
        implements this interface

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

        This method must be implemented in all classes that
        implements this interface

        Returns
        --------
        Any
            The data that was read.
        """
        ...

    def update_data(self, data: Any) -> bool:
        """
        Method to update some data in the database.

        This method must be implemented in all classes that
        implements this interface.

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

        This method must be implemented in all classes that
        implements this interface.

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
