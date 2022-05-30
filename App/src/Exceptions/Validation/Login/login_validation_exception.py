"""
Module containing all the exceptions related to the login validations.
"""

from App.src.Exceptions.Validation.validation_exceptions import ValidationException


class LoginValidationException(ValidationException):
    """
    Class to represent a generic exception that should be raised when
    some problem was found during the login validation.
    """


class UserNotFoundException(LoginValidationException):
    """
    Class to represent an exception that should be raised when
    the provided user was not found in the database during the login validation.
    """


class PasswordIncorrectException(LoginValidationException):
    """
    Class to represent an exception that should be raised when
    the provided password is incorrect during the login validation.
    """
