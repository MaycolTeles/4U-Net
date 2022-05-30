"""
Module containing all routes related to errors.
"""

from flask import Blueprint, render_template

from typing import Any, Tuple


error_routes = Blueprint("error_routes", __name__)


# ROUTES:
@error_routes.app_errorhandler(404)
def page_not_found(error: Any) -> Tuple[str, int]:
    """
    Function to create and render a generic error page (404).

    Parameters
    -----------
    error : Any
        The error. This parameter is passed automatically.

    Returns
    --------
    Tuple[str, int]:
        str:
            The error page rendered in str format
        int:
            The error code.
    """
    return render_template("Common/error_404.html"), 404
