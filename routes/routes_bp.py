from flask import Blueprint
from routes.routes import home

frases_bp = Blueprint('user_bp', __name__)

frases_bp.route('/', methods=['GET'])(home)