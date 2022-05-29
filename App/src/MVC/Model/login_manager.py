"""
Module containing the 'LoginManager' Class.
"""

from flask import Flask, flash
from flask_login import LoginManager as LoginManagerClass, UserMixin

from App.src.Entities.SQLAlchemy.user import User
from App.src.Interfaces.MVC.Model.database_interface import Database

from App.src.Exceptions.Login.login_validation_exception import *
from App.src.Exceptions.Register.register_validation_exceptions import *


class LoginManager(LoginManagerClass, Database):
    """
    Class to represent the LoginManager.

    This class implements the 'Database' Interface,
    so it must implement all the 'Database' functionalities, like:
    
    - Handling database queries.

    This Class implements an Interface to respect the DIP
    (Dependency Inversion Principle).
    """

    def connect(self, app: Flask) -> bool:
        """
        Method to connect to the LoginManager.

        Parameters
        -----------
        app : Flask
            The Flask application to initialize the LoginManager.

        Returns
        --------
        bool
            - True if connection was successfully established;
            - False otherwise.
        """
        try:
            self.init_app(app)

        except Exception as e:
            print('ERROR!')
            print(f'Error while trying to create a LoginManager. Error: {e}')
            return False

        return True

    def close(self) -> bool:
        """
        Method to close the LOginManager connection.

        Returns
        --------
        bool
            - True if connection was successfully closed;
            - False otherwise.
        """

    def validate_register(
        self,
        username: str,
        email: str,
        password: str,
        password_confirmation: str
    ) -> bool:
        """
        Method to validade the fields needed to register a new user.

        Parameters
        -----------
        username : str
            The user name.

        email : str
            The user email.        

        password : str
            The user password.

        password_confirmation : str
            The confirmation of the user password.

        Returns
        --------
        bool:
            - True if the user can be registered.
            - Raises an exception otherwise.

        Raises
        --------
        ValidationException:
            If the .
        """

        validations = [
            self.validate_register_username,
            self.validate_register_email,
            self.validate_register_password
        ]

        validations_params = [
            username,
            email,
            (password, password_confirmation)
        ]

        # EXECUTING ALL VALIDATIONS
        for validation, params in zip(validations, validations_params):

            try:
                res = validation(params)
            
            except RegisterValidationException as e:
                flash(e, category='error')
                return False
        
        return True

    def validate_register_username(self, username: str) -> bool:
        """
        Method to validade the username.

        Parameters
        -----------
        username : str
            The username.

        Returns
        --------
        bool
            - True if the username is available to use;
            - Raises an exception otherwise.

        Raises
        -------
        UsernameAlreadyExistsException
            If the provided username is already in the database.
        """
        username_exists = User.query.filter_by(username=username).first()

        if username_exists:
            raise UsernameAlreadyExistsException(
                'This username is already in use.'
                'Please, choose a different one.'
            )
        
        return True

    def validate_register_email(self, email: str) -> bool:
        """
        Method to validade the user email.

        Parameters
        -----------
        email : str
            The user email.

        Returns
        --------
        bool
            - True if the email is available to use;
            - Raises an exception otherwise.

        Raises
        -------
        EmailAlreadyExistsException
            If the provided email is already in the database.

        EmailInvalidException
            If the provided email is invalid.
        """
        email_exists = User.query.filter_by(email=email).first()

        if email_exists:
            raise EmailAlreadyExistsException(
                'This email is already in use.'
                'Please, choose a different one.'
            )

        if len(email) < 5 or '@' not in email:
            raise EmailInvalidException(
                'The provided e-mail is invalid.'
                'Please, choose your email correctly.'
            )
        
        return True

    def validate_register_password(
        self,
        password: str,
        password_confirmation: str
    ) -> bool:
        """
        Method to validade the user password.

        Parameters
        -----------
        password : str
            The user password.

        password_confirmation : str
            The user password confirmation.

        Returns
        --------
        bool
            - True if the password is available to use;
            - Raises an exception otherwise.

        Raises
        -------
        PasswordsDoesntMatchException
            If the provided password is different than the provided
            password confirmation.

        PasswordNotStrongException
            If the provided password is invalid (too short/weak).
        """
        if password != password_confirmation:
            raise PasswordsDoesntMatchException(
                'The passwords doesn\t match.'
                'Please, try again.'
            )

        if len(password) < 6:
            raise PasswordNotStrongException(
                'The password is too short.'
                'Please, choose a stronger one.'
            )

        return True


login_manager = LoginManager()


@login_manager.user_loader
def load_user() -> UserMixin:
    """
    Method to load the user

    Parameters
    -----------
    id : str
        The user id.

    Returns
    -----------
    UserMixin:
        The current user.
    """
    return User.query.get(int(id))
