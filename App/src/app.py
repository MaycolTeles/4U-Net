"""
Module containing the 'App' Class.
"""

from flask import Flask

from os import path

from flask_login import UserMixin

from App.config import TEMPLATE_FOLDER_PATH, STATIC_FOLDER_PATH
from App.config import DB_NAME
from App.config import FLASK_SECRET_KEY

from App.src.Interfaces.MVC.Model.database_interface import Database
from App.src.Interfaces.MVC.View.route_interface import Route


class App:
    """
    Class containing all the app functionalities.
    """

    app: Flask

    def __init__(
        self,
        database: Database,
        login_manager: Database,
        routes: Route,
        ) -> Flask:
        """
        Constructor used to create a reference to:
        * The Database;
        * The Login Manager;
        * The Routes;

        Parameters
        -----------
        database : Database
            A reference to the Database.

        login_manager : LoginManager
            A reference to the Login Manager.

        routes : Route
            A reference to all the app routes.

        Returns
        -----------
        Flask:
            A reference to the created Flask app.
        """
        self.app = Flask(
            __name__,
            template_folder=TEMPLATE_FOLDER_PATH,
            static_folder=STATIC_FOLDER_PATH
        )
        self.__db = database
        self.__login_manager = login_manager
        self.__routes = routes

        self.__config()

    def __config(self) -> None:
        """
        Method to config the app.

        Used to setup some configurations and variables.
        """
        self.app.config['SECRET_KEY'] = FLASK_SECRET_KEY
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
        self.__login_manager.login_view = 'src.MVC.View.Routes.common_routes'

        self.__create_routes()

    def __create_routes(self) -> None:
        """
        Private method to create all the app routes.
        """
        self.__routes.create_routes(self.app)

    def run(self) -> None:
        """
        Method to run the app.
        """
        # TODO: REMOVE THE DEBUG WHEN FINISHED
        self.app.run(debug=True)
