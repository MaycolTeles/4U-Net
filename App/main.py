"""
Main module containing the start of your application.
"""

from src.Entities.app import App


def main() -> None:
    """
    Main function. This is where your application will start.
    """

    app = App()
    app.run()


if __name__ == '__main__':
    main()
