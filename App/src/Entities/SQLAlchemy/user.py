"""
Module containing the 'User' Class.
"""

from flask_login import UserMixin
from sqlalchemy.sql import func

from dataclasses import dataclass

from App.src.MVC.Model.SQLAlchemy_model import database as db


@dataclass
class User(db.Model, UserMixin):
    """
    Class containing all the attributes (or colunms)
    for the User Entity.
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
