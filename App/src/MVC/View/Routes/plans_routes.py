"""
Module containing the 'PlansRoutes' Class.
"""

from flask import Flask, render_template


from src.Entities.API.ViasatAPI.plans_api import APIPlans

from src.Interfaces.MVC.View.route_interface import Route


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
        app.add_url_rule('/planos/', view_func=self.plans)
        app.add_url_rule('/planos/<plan_id>', view_func=self.plan)

    # ROUTES:
    def plans(self) -> str:
        """
        Method to render the page containing all plans.

        Returns
        --------
        str:
            The plans page rendered in str format.
        """
        plans = self.api.get_plans()

        return render_template(
            'Plans/plans.html',
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
