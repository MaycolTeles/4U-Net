"""
Module containing the 'App' Class.
"""

from flask import Flask

from App.config import TEMPLATE_FOLDER_PATH, STATIC_FOLDER_PATH
from App.config import DB_NAME
from App.config import FLASK_SECRET_KEY


class FlaskApp:
    """
    Class containing all the app functionalities.
    """

    __app: Flask

    def __init__(
        self,
        database,
        login_manager,
        routes,
    ) -> None:
        """
        Constructor used to create a reference to:
        * The Database;
        * The Login Manager;
        * The App Routes;

        Parameters
        -----------
        database : SQLAlchemyModel
            A reference to the SQLAlchemyModel.

        login_manager : LoginManagerModel
            A reference to the Login Manager.

        routes : Route
            A reference to all the app routes.
        """
        self.__app = Flask(
            __name__,
            template_folder=TEMPLATE_FOLDER_PATH,
            static_folder=STATIC_FOLDER_PATH
        )
        self.__db = database
        self.__login_manager = login_manager
        self.__routes = routes

        self.__configure()

    def __configure(self) -> None:
        """
        Method to config the app.

        Used to setup some configurations and variables.
        """
        self.__app.config['SECRET_KEY'] = FLASK_SECRET_KEY
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

        self.__db.connect(self.__app)

        # TODO: CHECK IF THIS WORKS
        # self.__login_manager.connect(self.__app)

        self.__create_routes()

        # TODO: CHECK IF CAN REMOVE THIS TEMP. FUNCTIONS
        self.temp_func()
        

    def __create_routes(self) -> None:
        """
        Private method to create all the app routes.
        """
        self.__routes.register_blueprints(self.__app)

    def run(self) -> None:
        """
        Method to run the app.
        """
        # TODO: REMOVE THE DEBUG WHEN FINISHED
        self.__app.run(debug=True)


    def temp_func(self):
        """
        ...
        """
        self.__db.create_database(self.__app)

        from App.src.MVC.View.Routes.common_routes import common_routes
        self.__login_manager.login_view = "common_routes.login"

        self.__login_manager.connect(self.__app)
