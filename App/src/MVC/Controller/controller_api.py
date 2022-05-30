"""
Module containing the 'APIController' Class.
"""

from typing import Dict

from App.config import JSON

from App.src.Interfaces.Entities.API.api_interface import API
from App.src.Interfaces.MVC.Controller.controller_api_interface import ControllerAPIInterface


class ControllerAPI(ControllerAPIInterface):
    """
    Class containing all the API controller responsabilities, like:
    
    - ...
    """

    def __init__(self, api: API) -> None:
        """
        ...
        """
        self.api = api

    def get_all_data(self) -> JSON:
        """
        ...
        """
        return self.api.get_all_data()

    def get_data_from_params(self, params: Dict[str, str]) -> JSON:
        """
        ...
        """
        return self.api.get_data_from_params(params)
