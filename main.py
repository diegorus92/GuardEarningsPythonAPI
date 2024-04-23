from flask import Blueprint
from .DataLayer.Data.database import Database


main_blueprint = Blueprint('main', __name__)

database = Database()
db = database.get_database_context()

@main_blueprint.route('/')
def welcome_msg():
    return 'Welcome to Guard Earnings API'
