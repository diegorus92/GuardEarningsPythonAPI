from flask import jsonify
from ...main import db
from ...DataLayer.Models.models import Guard
from bson import ObjectId


def get_guards_json():
    guards = list(db.guard.find())
    return jsonify(str(guards))

def get_guard_by_id(guard_id):
    return jsonify(str(db.guard.find_one({'_id': ObjectId(str(guard_id))})))

def get_guard_id_by_fullname(name, lastname):
    return db.guard.find_one({'$and': [{'name': name}, {'last_name': lastname}]}, {"_id": 1}).get('_id')


#Recomend to use only for print in console
def get_guards_as_str():
    guards = []
    result = list(db.guard.find())
    for item in result:
        guards.append(Guard(item['_id'], item['name'], item['last_name'],
                            item['date_of_birth'], item['email']))

    #print(list(map(lambda g: g.__str__(), guards)))
    return list(map(lambda g: g.__str__(), guards))


