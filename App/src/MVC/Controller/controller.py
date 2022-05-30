"""
Module containing the 'Controller' Class.
"""

# TYPE HINTS/ANNOTATIONS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from App.src.MVC.Model.SQLAlchemy_model import SQLAlchemyModel
    from App.src.MVC.Model.login_manager_model import LoginManagerModel


# IMPORTS
from flask import request, redirect, url_for, flash


class Controller():
    """
    Class containing all the controller responsabilities, like:
    
    - Handling user inputs received from the View Layer.
    - Calling the Model functions to communicate with the database.
    """

    def __init__(
        self,
        database: SQLAlchemyModel,
        login_manager: LoginManagerModel
    ) -> None:
        """
        ...
        """
        self.database = database
        self.login_manager = login_manager

    def handle_register_post(self) -> None:
        """
        Method to handle the 'POST' http method at the 'register' page.
        """
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")

        # CHECKING IF THE USER CREDENTIALS ARE OK
        validated = self.login_manager.register(
            username=username,
            email=email,
            password=password,
            password_confirmation=password_confirmation
        )

        if not validated:
            return

        # CHECKING IF THE USER WAS CREATED
        created = self.database.add_user(username, email, password)

        if not created:
            return 

        # ALREADY LOGGIN THE USER
        logged_in = self.login_manager.login(email=email, password=password)

        if not logged_in:
            return

        # USER SUCCESSFULLY CREATED
        flash('User created!', category='success')
        return redirect(url_for('index'))

    def handle_login_post(self) -> None:
        """
        Function to handle the 'POST' http method at the 'login' page.
        """
        email = request.form.get("email")
        password = request.form.get("password")

        # CHECKING IF USER WAS SUCCESSFULLY LOGGED IN
        logged_in = self.login_manager.login(email=email, password=password)

        if not logged_in:
            return

        # USER SUCCESSFULLY LOGGED IN
        flash("Logged in!", category='success')
        return redirect(url_for('index'))


from App.src.MVC.Model.SQLAlchemy_model import database
from App.src.MVC.Model.login_manager_model import login_manager

controller = Controller(database, login_manager)
