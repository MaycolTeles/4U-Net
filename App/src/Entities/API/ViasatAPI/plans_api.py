"""
Module containing the 'APIPlans' Class.
"""

import requests


from config import API_URL, JSON


class APIPlans():
    """
    Class containing all the plans API functionalities, like:
    
    - Consulting available plans;
    """

    def get_plans(self) -> JSON:
        """
        Method to return all the plans from the api.

        Returns
        -------
        JSON:
            All the available plans.
        """
        res = requests.get(API_URL + '/plans')
        return res.json()

    def get_plan_from_plan_id(self, plan_id: str) -> JSON:
        """
        Method to return the plan that matches the plan id
        received as argument.

        Parameters
        ----------
        plan_id : str
            The plan id to consult

        Returns
        ---------
        JSON:
            The correspondent plan that matches the 'plan_id' if it exists.
        """
        res = requests.get(API_URL + '/plans/' + plan_id)
        return res.json()

    def get_plans_from_installer_id(self, installer_id: str) -> JSON:
        """
        Method to return all the plans that are available to the
        specific installer, based on his id received as argument.

        Parameters
        ----------
        installer_id : str
            The installer id to consult

        Returns
        ---------
        JSON:
            All the correspondent plans that matches the 'installer_id'
            if it exists.
        """
        res = requests.get(API_URL + '/plans?installer=' + installer_id)
        return res.json()

    def get_plans_from_state(self, state: str) -> JSON:
        """
        Method to return all the plans that are available to that state
        based on the state received as argument.

        Parameters
        ----------
        state : str
            The state to consult

        Returns
        ---------
        JSON:
            All the correspondent plans that matches the 'state'
            if it exists.
        """
        res = requests.get(API_URL + '/plans?state=' + state)
        return res.json()
