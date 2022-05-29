"""
Module containing the 'Installer' Class.
"""

from dataclasses import dataclass

from App import database as db
from App.src.Entities.SQLAlchemy.user import User


@dataclass
class Installer(User):
    """
    Class containing all the attributes (or colunms)
    for the Installer Entity.
    """

    plans = db.Column(db.PickleType, primary_key=True)
