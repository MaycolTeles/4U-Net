"""
Module containing the 'App' Class.
"""

from flask import Flask

from config import TEMPLATE_FOLDER_PATH
from src.MVC.View.routes import Routes


class App:
    """
    Class containing all the app functionalities.
    """

    app: Flask

    def __init__(self, routes: Routes) -> None:
        """
        Constructor to create a reference and initialize the app.
        """
        self.__app = Flask(__name__, template_folder=TEMPLATE_FOLDER_PATH)
        self.__routes = routes

        self.__create_routes()

    def __create_routes(self) -> None:
        """
        Private method to create all the app routes.
        """
        self.__routes.create_routes(self.__app)

    def run(self) -> None:
        """
        Method to run the app.
        """
        # TODO: REMOVE THE DEBUG WHEN FINISHED
        self.__app.run(debug=True)
