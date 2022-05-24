"""
Module containing the 'App' Class.
"""

from flask import Flask
from src.Routes.routes import Routes as route
from src.Routes.routes import ClientRoutes as client_route
from src.Routes.routes import InstallerRoutes as installer_route


TEMPLATE_FOLDER_PATH = '../../templates'


class App:
    """
    Class containing all the app functionalities.
    """

    app: Flask

    def __init__(self) -> None:
        """
        Constructor to create a reference and initialize the app.
        """
        self.app = Flask(__name__, template_folder=TEMPLATE_FOLDER_PATH)

        self.__create_routes()

    def __create_routes(self) -> None:
        """
        Private method to create all the app routes.
        """
        self.app.add_url_rule('/', view_func=route.index)
        self.app.add_url_rule('/cliente/<client_name>', view_func=client_route.clients)
        self.app.add_url_rule('/instalador/<installer_name>', view_func=installer_route.installers)

    def run(self) -> None:
        """
        Method to run the app.
        """
        # TODO: REMOVE THE DEBUG WHEN FINISHED
        self.app.run(debug=True)
