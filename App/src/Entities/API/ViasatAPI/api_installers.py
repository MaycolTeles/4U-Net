"""
Module containing the 'APIInstallers' Class.
"""

import requests

from typing import Tuple

from App.config import API_URL, JSON
from App.src.Interfaces.Entities.API.api_interface import API


class APIInstallers(API):
    """
    Class containing all the API functionalities,
    related to the installers, like:
    
    - Consulting all available installers;
    - Consulting availables installers based on a param;

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    # IMPLEMENTING THE INTERFACE's METHODS
    def get_all_data(self) -> JSON:
        """
        Method to return all data from the API,
        related to the installers.

        Returns
        --------
        JSON:
            The data in a JSON format.
        """
        return self.__get_all_installers()

    def get_data_from_params(self, params: Tuple[str, str]) -> JSON:
        """
        ...
        """
        methods = {
            'installer_id': self.__get_installer_from_installer_id,
            'plan_id': self.__get_installers_from_plan_id,
        }

        param_name = params[0]
        param_value = params[1]

        data = None

        if param_name in methods:
            data = methods[param_name](param_value)

        if not data:
            return

        return data

    def __get_all_installers(self) -> JSON:
        """
        Method to return all the installers from the api.

        Returns
        -------
        JSON:
            All the available installers.
        """
        return requests.get(API_URL + '/installers')

    def __get_installer_from_installer_id(self, installer_id: str) -> JSON:
        """
        Method to return the installer based on his id received as argument.

        Parameters
        ----------
        installer_id : str
            The installer id to consult

        Returns
        ---------
        JSON:
            The correspondent installer that matches the 'installer_id'
            if it exists.
        """
        return requests.get(API_URL + '/installers/' + installer_id).json()

    def __get_installers_from_plan_id(self, plan_id: str) -> JSON:
        """
        Method to return all the installers that matches the plan id
        received as argument.

        Parameters
        ----------
        plan_id : str
            The plan id to consult

        Returns
        ---------
        JSON:
            All the installers that matches the 'plan_id' if it exists.
        """
        return requests.get(API_URL + '/installers?plan=' + plan_id).json()
