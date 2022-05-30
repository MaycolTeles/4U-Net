"""
Module containing the 'API' Interface.
"""

from typing import Protocol

from App.config import JSON


class API(Protocol):
    """
    Interface to represent an API.

    This interface contains all the 'API' functionalities, like:
    
    - Handling and formatting API data;

    This is an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def format_data(self, data: JSON) -> JSON:
        """
        Method to format the received data.

        Parameters
        ----------
        data : JSON
            The data to be formatted.

        Returns
        -------
        JSON:
            The formatted data.
        """
