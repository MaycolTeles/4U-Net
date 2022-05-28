"""
Module containing some configurations and constants.
"""

from dotenv import load_dotenv

import os
from typing import Any, Dict


JSON = Dict[str, Any]

TEMPLATE_FOLDER_PATH = '../templates'

STATIC_FOLDER_PATH = '../static'

API_URL = 'https://app-challenge-api.herokuapp.com'


# DATABASE
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
