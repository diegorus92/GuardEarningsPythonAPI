from flask import Blueprint, request
from .DataLayer.Data.database import Database
from .BussinesLayer.Operations.calculus import TimeOperation


main_blueprint = Blueprint('main', __name__)

database = Database()
db = database.get_database_context()

@main_blueprint.route('/')
def welcome_msg():
    return 'Welcome to Guard Earnings API'

@main_blueprint.route('/test')
def test():
    time = TimeOperation()
    return str(time.calculate_total_hours(request.args.get("checkIn"), request.args.get("checkOut"))) + " total hours"
