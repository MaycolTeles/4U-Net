"""
Module containing the 'API' Interface.
"""

from typing import Protocol, Tuple

from App.config import JSON


class API(Protocol):
    """
    Interface to represent an API.

    This interface contains all the 'API' functionalities, like:
    
    - Retrieving all data;
    - Retrieving data based on parameters.

    This is an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def get_all_data(self) -> JSON:
        """
        Method to return the data from the API without any parameters.

        Returns
        --------
        JSON:
            The full data correctly formatted.
        """

    def get_data_from_params(self, params: Tuple[str, str]) -> JSON:
        """
        Method to return the data from the API without any parameters.

        Returns
        --------
        JSON:
            The full data correctly formatted.
        """
