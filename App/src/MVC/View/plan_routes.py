"""
Module containing the 'PlanRoutes'.
"""

from flask import Flask, render_template

from src.Interfaces.MVC.View.route_interface import Route


class PlanRoutes(Route):
    """
    Class containing all the Plan Routes.
    """

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all the common routes.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
        app.add_url_rule('/plans', view_func=self.plans)
        app.add_url_rule('/plano/<plan_name>', view_func=self.plano)

    # ROUTES:
    def plans(self) -> str:
        """
        Method to render the plans page.

        Returns
        --------
        str:
            The plans page rendered in str format.
        """
        return render_template('plans.html')

    def plan(self, plan_name: str) -> str:
        """
        Method to render the plan page, based on a single plan.

        Parameters
        ----------
        plan_name : str
            The plan name

        Returns
        --------
        str:
            The plans page rendered in str format.
        """
        return render_template('plans.html', plan_name=plan_name)
