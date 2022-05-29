"""
Module containing all the exceptions related to the register validations.
"""

from src.Exceptions.validation_exceptions import ValidationException


class RegisterValidationException(ValidationException):
    """
    Class to represent a generic exception that should be raised when
    some problem was found during the register validation.
    """


class UsernameAlreadyExistsException(RegisterValidationException):
    """
    Class to represent an exception that should be raised when
    the provided username is already in the database
    during the register validation.
    """


class EmailAlreadyExistsException(RegisterValidationException):
    """
    Class to represent an exception that should be raised when
    the provided email is already in the database
    during the register validation.
    """


class EmailInvalidException(RegisterValidationException):
    """
    Class to represent an exception that should be raised when
    the provided email is invalid during the register validation.
    """


class PasswordsDoesntMatchException(RegisterValidationException):
    """
    Class to represent an exception that should be raised when
    the provided passwords does not match during the register validation.
    """


class PasswordNotStrongException(RegisterValidationException):
    """
    Class to represent an exception that should be raised when
    the provided password isn't strong enough during the register validation.
    """
