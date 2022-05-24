"""
Module containing the 'InstallerRoutes'.
"""

from flask import render_template


class InstallerRoutes():
    """
    Class containing all the Installer Routes.
    """

    @staticmethod
    def installers(installer_name: str) -> str:
        """
        Method to render the installer page.

        Parameters
        ----------
        installer_name : str
            The installer name

        Returns
        --------
        str:
            The installers page rendered in str format.
        """
        return render_template('installers.html', installer_name=installer_name)
