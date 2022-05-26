"""
Main module containing the application start.
"""

from src.app import App
from src.MVC.View.routes import Routes


def main() -> None:
    """
    Main function. This is where the application will start.
    """

    routes = Routes()

    app = App(routes)
    app.run()


if __name__ == '__main__':
    main()