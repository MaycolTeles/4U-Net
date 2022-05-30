"""
Module containing the 'Client' Class.
"""

from dataclasses import dataclass

from App import database as db
from App.src.Entities.SQLAlchemy.user import User


@dataclass
class Client(User):
    """
    Class containing all the attributes (or colunms)
    for the Client Entity.
    """

    plans = db.Column(db.String(100), primary_key=True)
