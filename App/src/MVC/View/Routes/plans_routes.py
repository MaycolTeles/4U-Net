"""
Module containing the all routes related to the plans.
"""

from flask import Blueprint, redirect, render_template, request, url_for

from App.config import HTTP_METHODS
from App.src.Utils import utils

from App.src.Entities.API.ViasatAPI.api_plans import APIPlans
from App.src.MVC.Controller.controller_api import ControllerAPI


plans_routes = Blueprint('plans_routes', __name__)

controller_api = ControllerAPI(APIPlans())


# ROUTES:
@plans_routes.route('/escolher-estado/')
def choose_state() -> str:
    """
    Function to create the '/escolher-estado' route and
    render the page to choose a state.

    Returns
    --------
    str:
        The page to choose the state rendered in str format.
    """
    return render_template('Plans/choose_state.html')


@plans_routes.route('/todos/')
def all_plans() -> str:
    """
    Function to create the '/' route and
    render the page containing all plans.

    Returns
    --------
    str:
        The plans page rendered in str format.
    """
    plans = controller_api.get_all_data()

    return render_template(
        'Plans/all_plans.html',
        plans=plans,
        len_plans=len(plans)
    )


@plans_routes.route('/planos/', methods=HTTP_METHODS)
def plans_from_state() -> str:
    """
    Function to create the '/planos' route and
    render the page containing all plans from the chosen state.

    Returns
    --------
    str:
        The plans page containing all the plans
        that their states are equal to the state received as argument,
        rendered in str format.
    """
    if request.method == 'GET':
        return render_template(
            'Plans/plans_from_state.html',
            state=utils.convert_state_initials_to_full_name(state),
            plans=plans,
            len_plans=len(plans)
        )

    state = request.form.get('state')

    if state == 'Todos':
        return redirect(url_for('plans_routes.all_plans'))

    return redirect(url_for('plans_routes.plans_from_choosen_state', state=state))


@plans_routes.route('/<state>/', methods=HTTP_METHODS)
def plans_from_choosen_state(state: str) -> str:
    """
    Function to create the '/planos' route and
    render the page containing all plans from the chosen state.

    Parameters
    -----------
    state : str
        The choosen state.

    Returns
    --------
    str:
        The plans page containing all the plans
        that their states are equal to the state received as argument,
        rendered in str format.
    """
    plans = controller_api.get_data_from_params(('state', state))

    return render_template(
        'Plans/plans_from_state.html',
        state=utils.convert_state_initials_to_full_name(state),
        plans=plans,
        len_plans=len(plans)
    )


@plans_routes.route('/<plan_id>')
def plan(plan_id: str) -> str:
    """
    Function to create the '/<plan_id>' route and
    render the page containing a single plan,
    according to the id received as argument.

    Parameters
    ----------
    plan_id : str
        The plan id

    Returns
    --------
    str:
        The plans page rendered in str format.
    """
    plan = controller_api.get_data_from_params(('plan_id', plan_id))

    return render_template('Plans/plan.html', plan=plan)
