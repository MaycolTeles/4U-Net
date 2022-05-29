"""
Module containing the 'PlansRoutes' Class.
"""

from flask import Flask, render_template, request

from App.config import JSON, HTTP_METHODS

from App.src.Entities.API.ViasatAPI.plans_api import APIPlans

from App.src.Interfaces.MVC.View.route_interface import Route

from App.src.Utils import utils


class PlansRoutes(Route):
    """
    Class containing all the Plans Routes.
    """

    def __init__(self, api: APIPlans) -> None:
        """
        Constructor the create a reference to the Plans API.
        """
        self.api = api

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all the plan routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        app.add_url_rule('/planos/', view_func=self.all_plans)
        app.add_url_rule('/planos/escolher_estado', view_func=self.choose_state)
        app.add_url_rule('/planos/', methods=HTTP_METHODS, view_func=self.plans_from_state)
        app.add_url_rule('/planos/<plan_id>', view_func=self.plan)

    # ROUTES:
    def choose_state(self) -> str:
        """
        Method to render the page to choose a state.

        Returns
        --------
        str:
            The page to choose the state rendered in str format.
        """
        return render_template('Plans/choose_state.html')

    def all_plans(self) -> str:
        """
        Method to render the page containing all plans.

        Returns
        --------
        str:
            The plans page rendered in str format.
        """
        plans = self.api.get_plans()

        return render_template(
            'Plans/all_plans.html',
            plans=plans,
            len_plans=len(plans)
        )

    def plans_from_state(self) -> str:
        """
        Method to render the page containing all plans from the chosen state.

        Returns
        --------
        str:
            The plans page containing all the plans
            that their states are equal to the state received as argument,
            rendered in str format.
        """
        state = request.form.get('state_select')

        if state == 'Todos':
            return self.all_plans()

        plans = self.api.get_plans_from_state(state)

        return render_template(
            'Plans/plans_from_state.html',
            state=utils.convert_state_initials_to_full_name(state),
            plans=plans,
            len_plans=len(plans)
        )

    def plan(self, plan_id: str) -> str:
        """
        Method to render the page containing a single plan,
        which the id was received as argument.

        Parameters
        ----------
        plan_id : str
            The plan id

        Returns
        --------
        str:
            The plans page rendered in str format.
        """
        plan = self.api.get_plan_from_plan_id(plan_id)

        return render_template('Plans/plan.html', plan=plan)
