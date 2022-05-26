"""
Module containing the 'Route' Interface.
"""

from flask import Flask

from typing import Protocol


class Route(Protocol):
    """
    Interface to represent a Route.

    This interface contains all the 'Route' functionalities, like:
    
    - Creating all routes.

    This is an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def create_routes(self, app: Flask) -> None:
        """
        Method to create all routes.

        This method must be implemented in all classes that
        implements this interface.

        Parameters
        -----------
        app : Flask
            A reference to the Flask app.
        """
