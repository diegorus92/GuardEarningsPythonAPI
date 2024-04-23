from flask import Blueprint, request
from ...BussinesLayer.Services import workService

worksController_blueprint = Blueprint('worksController0', __name__)


@worksController_blueprint.route('/get-works')
def get_works():
    return workService.get_works_json()

@worksController_blueprint.route('/get-works-by-guard-fullname')
def get_works_by_guard_fullname(): #Require Json as argument from request
    req = request.get_json()
    return workService.get_works_by_guard_fullname(req['name'], req['lastname'])

    #For pass arguments from URL params
    #return workService.get_works_by_guard_fullname(str(request.args.get('name')), str(request.args.get('lastname')))

@worksController_blueprint.route('/get_works_by_guard_and_month_year')
def get_works_by_guard_and_month_year():
    req = request.get_json()
    return workService.get_works_by_guard_and_month_year(req['name'], req['lastname'], req['month'], req['year'])



