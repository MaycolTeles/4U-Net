"""
Module containing the 'UI' Interface.
"""

from typing import Protocol


class UI(Protocol):
    """
    Interface to represent a User Interface.

    This interface contains all the 'UI' functionalities, like:
    
    - Reading user inputs.
    - Showing some informations for the user.

    This is an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def show(self, msg: str) -> None:
        """
        Method to show some message or text to the user.

        This method must be implemented in all classes that
        implements this interface.

        Parameters
        -----------
        msg : str
            The message to be showed to the user.
        """
        ...

    def get_input(self) -> str:
        """
        Method to get some input from the user.

        This method must be implemented in all classes that
        implements this interface.

        Returns
        -----------
        str
            The user input.
        """
        ...
