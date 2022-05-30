"""
Module containing some configurations and constants.
"""

from dotenv import load_dotenv

import os
from typing import Any, Dict


JSON = Dict[str, Any]

HTTP_METHODS = ['GET', 'POST']

TEMPLATE_FOLDER_PATH = '../templates'

API_URL = 'https://app-challenge-api.herokuapp.com'


# ENV VARIABLES
load_dotenv()

FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

DB_NAME = os.getenv('DB_NAME')
