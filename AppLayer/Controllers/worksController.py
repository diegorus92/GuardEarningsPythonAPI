from flask import Blueprint, request
from ...BussinesLayer.Services import workService
import json

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
    return workService.get_works_by_guard_and_month_year(req['guard_name'], req['guard_lastname'], req['date_month'], req['date_year'])

@worksController_blueprint.route('/insert-new-work-to-guard', methods=['POST'])
def insert_workday_to_guard():
    req = request.get_json()
    return workService.insert_workday_to_guard(
        req['guard_name'], req['guard_lastname'], req['date_day'], req['date_month'],
        req['date_year'], req['type_place'], req['name_place'],
        req['address'], req['checkIn'], req['checkOut'], req['payment'])



@worksController_blueprint.route("/get-payment-per-day")
def get_payment_per_day():
    req = request.get_json()
    works = workService.get_payment_per_day(req["guard_name"],
                                            req["guard_lastname"],
                                            req["date_month"],req["date_year"])
    return works

@worksController_blueprint.route("/get-resume-for-month")
def get_resume_for_month():
    req = request.get_json()
    resume = workService.get_resume_for_month(req["guard_name"],
                                              req["guard_lastname"],
                                              req["date_month"], req["date_year"])

    return {
        "payment_per_day": workService.get_payment_per_day(req["guard_name"], req["guard_lastname"],
                                                           req["date_month"], req["date_year"]),
        "resume": resume
    }
