"""
Module containing the 'CLI' Class.
"""

from App.src.Interfaces.MVC.View.UI_interface import UI


class CLI(UI):
    """
    Class to represent a Command Line Interface.

    This class implements the 'UI' Interface, so
    it has all the 'UI' functionalities, like:
    
    - Reading user inputs.
    - Showing some informations for the user.

    This Class implements an Interface to respect the DIP
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
