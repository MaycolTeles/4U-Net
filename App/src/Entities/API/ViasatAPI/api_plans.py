"""
Module containing the 'APIPlans' Class.
"""

import requests

from typing import Tuple

from App.config import API_URL, JSON
from App.src.Interfaces.Entities.API.api_interface import API


class APIPlans(API):
    """
    Class containing all the API functionalities,
    related to the plans, like:
    
    - Consulting all available plans;
    - Consulting availables plans based on a param;

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    # IMPLEMENTING THE INTERFACE's METHODS
    def get_all_data(self) -> JSON:
        """
        Method to return all data from the API,
        related to the plans.

        Returns
        --------
        JSON:
            The formated data in a JSON format.
        """
        data = self.__get_all_plans()
        return self.__format_data(data)

    def get_data_from_params(self, params: Tuple[str, str]) -> JSON:
        """
        Method to return the data from the API
        based on the parameters received as argument.

        Parameters
        -----------
        params : Dict[str, str]
            The parameters to send to the API call.

        Returns
        --------
        JSON:
            The formated data in a JSON format.
        """
        methods = {
            'plan_id': self.__get_plan_from_plan_id,
            'installer_id': self.__get_plans_from_installer_id,
            'state': self.__get_plans_from_state
        }

        param_name = params[0]
        param_value = params[1]

        data = None

        if param_name in methods:
            data = methods[param_name](param_value)

        if not data:
            return

        return self.__format_data(data)

    def __get_all_plans(self) -> JSON:
        """
        Method to return all the plans from the api.

        Returns
        -------
        JSON:
            All the available plans.
        """
        return requests.get(API_URL + '/plans').json()

    def __get_plan_from_plan_id(self, plan_id: str) -> JSON:
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
        return requests.get(API_URL + '/plans/' + plan_id).json()

    def __get_plans_from_installer_id(self, installer_id: str) -> JSON:
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
        return requests.get(API_URL + '/plans?installer=' + installer_id).json()

    def __get_plans_from_state(self, state: str) -> JSON:
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
        return requests.get(API_URL + '/plans?state=' + state).json()

    def __format_data(self, data: JSON) -> JSON:
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
        type_of_internet_replaces = {
            'sat': 'Satélite',
            'wire': 'Cabeada',
            'cable': 'Cabeada',
            'radio': 'Rádio'
        }

        try:
            for item in data:

                # REPLACING THE 'data_capacity' KEY (if needed)
                if item['data_capacity'] is None:
                    item['data_capacity'] = 'Não informado'

                # REPLACING THE 'type_of_internet' KEY (if needed)
                if item['type_of_internet'] in type_of_internet_replaces:
                    item['type_of_internet'] = item['type_of_internet'].replace(
                        item['type_of_internet'],
                        type_of_internet_replaces[item['type_of_internet']]
                    )
        except Exception as e:
            print('ERROR!')
            print(f'Unable to retrieve data from the API. Error: {e}')
            return {}

        return data
