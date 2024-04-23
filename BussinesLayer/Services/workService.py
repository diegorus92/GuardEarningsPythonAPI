from bson import ObjectId

from ...main import db
from flask import jsonify
from . import guardService

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
