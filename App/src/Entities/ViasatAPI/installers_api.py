"""
Module containing the 'APIInstallers' Class.
"""

import requests

from config import API_URL, JSON


class APIInstallers():
    """
    Class containing all the Installers API functionalities, like:
    
    - Consulting available installers;
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
        return res.json()

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
        return res.json()

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
        return res.json()
