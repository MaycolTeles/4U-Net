"""
Module containing the 'APIInstallers' Class.
"""

import requests

from config import API_URL


class APIInstallers():
    """
    Class containing all the Installers API functionalities, like:
    
    - Consulting available installers;
    """

    def get_installers(self) -> str:
        """
        Method to return all the installers from the api.

        Returns
        -------
        str:
            All the available installers.
        """
        res = requests.get(API_URL + '/installers')
        return res.text

    def get_installers_from_installer_id(self, installer_id: str) -> str:
        """
        Method to return the installer based on his id received as argument.

        Parameters
        ----------
        installer_id : str
            The installer id to consult

        Returns
        ---------
        str:
            The correspondent installer that matches the 'installer_id'
            if it exists.
        """
        res = requests.get(API_URL + '/installers/' + installer_id)
        return res.text

    def get_installers_from_plan_id(self, plan_id: str) -> str:
        """
        Method to return all the installers that matches the plan id
        received as argument.

        Parameters
        ----------
        plan_id : str
            The plan id to consult

        Returns
        ---------
        str:
            All the installers that matches the 'plan_id' if it exists.
        """
        res = requests.get(API_URL + '/installers?plan=' + plan_id)
        return res.text
