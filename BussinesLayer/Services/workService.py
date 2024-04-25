import datetime
from ...main import db
from flask import jsonify
from . import guardService
from ...DataLayer.Models.models import work_structure_db, Work
from ..Operations.calculus import WorkOperation

def get_works_json():
    works = list(db.works.find())
    return jsonify((str(works)))

def get_works_by_guard_fullname(name, lastname):
    guard_id = guardService.get_guard_id_by_fullname(name, lastname)
    works = list(db.works.find({'guard_id': guard_id}))
    return jsonify(str(works))

def _get_works_by_guard_and_month_year_as_list(guardName, guardLastname, monthNumber, year):
    guard_id = guardService.get_guard_id_by_fullname(guardName, guardLastname)
    works = list(db.works.find({'$and': [
        {'guard_id': guard_id},
        {'date': {'$regex': f"-{monthNumber}-{year}"}}]}))
    return works

def get_works_by_guard_and_month_year(guardName, guardLastname, monthNumber, year):
    works = _get_works_by_guard_and_month_year_as_list(guardName, guardLastname, monthNumber, year)

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

def get_payment_per_day(guard_name, guard_lastname, date_month, date_year):
    raw_works = _get_works_by_guard_and_month_year_as_list(guard_name, guard_lastname, date_month, date_year)
    workList = []
    workOp = None

    for work_item in raw_works:
        workList.append(Work(work_item["_id"], work_item["guard_id"],
                             work_item["date"], work_item["place"],
                             work_item["address"], work_item["checkIn"], work_item["checkOut"],
                             work_item["payment_per_hours"], work_item["day"]))
    workOp = WorkOperation(workList)
    return workOp.calculate_payment_per_day()

def get_resume_for_month(guard_name, guard_lastname, date_month, date_year):
    raw_works = _get_works_by_guard_and_month_year_as_list(guard_name, guard_lastname, date_month, date_year)
    workList = []
    workOp = None

    for work_item in raw_works:
        workList.append(Work(work_item["_id"], work_item["guard_id"],
                             work_item["date"], work_item["place"],
                             work_item["address"], work_item["checkIn"], work_item["checkOut"],
                             work_item["payment_per_hours"], work_item["day"]))
    workOp = WorkOperation(workList)
    total_hours = workOp.calculate_total_hours()
    total_payment = workOp.calculate_total_payment()

    return {"total_days_worked": len(workList), "total_hours": total_hours, "total_payment": total_payment} #Add Total payment, Total days worked
