"""
Module containing the 'APIControllerInterface' Interface.
"""

from typing import Dict, Protocol

from App.config import JSON


class ControllerAPIInterface(Protocol):
    """
    Interface to represent a Controller to an API.

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

    def get_data_from_params(self, params: Dict[str, str]) -> JSON:
        """
        Method to return the data from the API without any parameters.

        Returns
        --------
        JSON:
            The full data correctly formatted.
        """
