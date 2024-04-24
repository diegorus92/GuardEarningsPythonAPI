import datetime

from bson import ObjectId

from ...main import db
from flask import jsonify
from . import guardService
from ...DataLayer.Models.models import work_structure_db

def get_works_json():
    works = list(db.works.find())
    return jsonify((str(works)))

def get_works_by_guard_fullname(name, lastname):
    guard_id = guardService.get_guard_id_by_fullname(name, lastname)
    works = list(db.works.find({'guard_id': guard_id}))
    return jsonify(str(works))

def get_works_by_guard_and_month_year(guardName, guardLastname, monthNumber, year):
    guard_id = guardService.get_guard_id_by_fullname(guardName, guardLastname)
    works = list(db.works.find({'$and': [
        {'guard_id': guard_id},
        {'date': {'$regex': f"-{monthNumber}-{year}"}}]}))

    return jsonify((str(works)))

def insert_workday_to_guard(guard_name, guard_lastname, date_day, date_month, date_year, type_place, name_place, address, checkIn, checkOut, payment):
    work_to_add = work_structure_db.copy()
    work_to_add.update({
        "guard_id": guardService.get_guard_id_by_fullname(guard_name, guard_lastname),
        "date": f"{date_day}-{date_month}-{date_year}",
        "place": f"{type_place}<{name_place}>",
        "address": address,
        "checkIn": checkIn,
        "checkOut": checkOut,
        "payment_per_hours": float(payment),
        "day": datetime.date(int(date_year), int(date_month), int(date_day)).strftime("%A").lower()
    })

    response = "Work posted: " + str(work_to_add)

    insertion_result = str(db.works.insert_one(work_to_add))
    return response + "\n" + insertion_result

