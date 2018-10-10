from flask import Flask

from imprint.db import get_db

bp = Blueprint('dashboard',__name__, url_prefix='/dashboard')
