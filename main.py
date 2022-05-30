"""
Main module containing the application start.
"""

from App import create_app


def main() -> None:
    """
    Main function. This is where the application will start.
    """

    app = create_app()
    app.run()


if __name__ == '__main__':
    main()
