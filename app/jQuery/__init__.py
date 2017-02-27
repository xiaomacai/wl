from flask import Blueprint

jQuery = Blueprint('jQuery', __name__)

from . import views
