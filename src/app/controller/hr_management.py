from flask import Blueprint, app, jsonify, request
import inject
from application.services import (UserService, DepartmentService)
from controller.utils   import (file_by_mimetype, filter_request_consistency)

@inject.autoparams()
def create_blueprint(userService: UserService, departmentService: DepartmentService) -> Blueprint:
    post_blueprint = Blueprint('post', __name__)

    @post_blueprint.route("/ping", methods=['GET'])
    def ping():
        return "pong"

    @post_blueprint.route("/userAdd", methods=['GET', 'POST'])
    def userAdd():
        if request.method == 'GET':
            return jsonify({'status': 'alive!'})
        userInfo = filter_request_consistency(request, int)
        # logging.warn(userInfo)
        return jsonify(userService.addUser(userInfo['id'], userInfo['description'], userInfo['userName'], userInfo['deptId']))

    @post_blueprint.route("/deptAdd", methods=['GET', 'POST'])
    def deptAdd():
        if request.method == 'GET':
            return jsonify({'status': 'alive!'})
        deptInfo = filter_request_consistency(request, int)
        # logging.warn(deptInfo)
        return jsonify(departmentService.addDepartment(deptInfo['id'], deptInfo['description'], deptInfo['deptName']))

    @post_blueprint.route("/userInfoDetail/<userId>", methods=['GET', 'POST'])
    def userInfoDetail(userId):
        if request.method == 'POST':
            return jsonify({'status': 'not accept POST method'})
        # userInfo = filter_request_consistency(request, int)
        return jsonify(userService.detailUser(userId))
    
    return post_blueprint