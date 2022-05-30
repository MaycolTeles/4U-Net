"""
Module containing the 'APIInstallers' Class.
"""

import requests


from App.config import API_URL, JSON

from App.src.Interfaces.Entities.API.api import API


class APIInstallers(API):
    """
    Class containing all the Installers API functionalities, like:
    
    - Consulting available installers;

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    # IMPLEMENTING THE INTERFACE's METHODS
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

    def get_installers(self) -> JSON:
        """
        Method to return all the installers from the api.

        Returns
        -------
        JSON:
            All the available installers.
        """
        res = requests.get(API_URL + '/installers')
        payload = self.format_data(res.json())
        return payload

    def get_installers_from_installer_id(self, installer_id: str) -> JSON:
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
        res = requests.get(API_URL + '/installers/' + installer_id)
        payload = self.format_data(res.json())
        return payload

    def get_installers_from_plan_id(self, plan_id: str) -> JSON:
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
        res = requests.get(API_URL + '/installers?plan=' + plan_id)
        payload = self.format_data(res.json())
        return payload
