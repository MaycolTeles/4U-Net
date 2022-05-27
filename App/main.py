"""
Main module containing the application start.
"""

from src.app import App
from src.MVC.View.Routes.routes import Routes


def main() -> None:
    """
    Main function. This is where the application will start.
    """

    routes = Routes()

    app = App(routes)
    app.run()


if __name__ == '__main__':
    main()

    # from src.Entities.ViasatAPI.plans_api import APIPlans

    # api = APIPlans()

    # plans = api.get_plans_from_state('SP')

    # for id, plan in enumerate(plans):
    #     print(f'PLANO {id}: {plan}\n')
