"""
Module containing all routes related to the installers.
"""

from flask import Blueprint, render_template

from App.src.Entities.API.ViasatAPI.api_installers import APIInstallers
from App.src.MVC.Controller.controller_api import ControllerAPI


installers_routes = Blueprint('installers_routes', __name__)
controller_api = ControllerAPI(APIInstallers())


# ROUTES:
@installers_routes.route('/')
def installers() -> str:
    """
    Function to create the '/' route and
    render the page containing all installers.

    Returns
    --------
    str:
        The installers page rendered in str format.
    """
    installers = controller_api.get_all_data()

    return render_template(
        'Installers/installers.html',
        installers=installers,
        len_installers=len(installers)
    )


@installers_routes.route('/<installer_id>')
def installer(installer_id: str) -> str:
    """
    Function to create the '/<installer_id>' route
    and render the page containing a single installer,
    which the id was received as argument.

    Parameters
    ----------
    installer_id : str
        The installer id

    Returns
    --------
    str:
        The installers page rendered in str format.
    """
    installer = controller_api.get_data_from_params(('installer_id', installer_id))

    return render_template('Installers/installer.html', installer=installer)
