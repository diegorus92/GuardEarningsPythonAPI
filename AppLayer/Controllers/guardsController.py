from flask import Blueprint, request
from ...BussinesLayer.Services import guardService

guardController_blueprint = Blueprint('guardController', __name__)

@guardController_blueprint.route('/get-guards')
def get_guards():
    return guardService.get_guards_json()

@guardController_blueprint.route('/get-guard')
def get_guard_by_id():
    return guardService.get_guard_by_id(request.args.get('guard_id'))

@guardController_blueprint.route('/get-guard-id')
def get_guard_id_by_fullname():
    return guardService.get_guard_id_by_fullname(str(request.args.get('name')), str(request.args.get('lastname')))
