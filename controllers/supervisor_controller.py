from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.supervisor import Supervisor
from services.supervisors_service import SupervisorService


def route(app):
    @app.route("/supervisors", methods=["POST"])
    def post_supervisor():
        try:
            supervisor = Supervisor.json_parse(request.json)
            supervisor = SupervisorService.add_supervisor(supervisor)
            return jsonify(supervisor.json()), 201
        except KeyError:
            return "Please enter two valid employee names.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/supervisors", methods=["GET"])
    def get_all_supervisors():
        return jsonify(SupervisorService.get_all_supervisors())

    @app.route("/supervisors/<employee_user>", methods=["GET"])
    def get_supervisor(employee_user):
        try:
            supervisor = SupervisorService.get_supervisor(employee_user)
            return jsonify(supervisor.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/supervisors/<employee_user>", methods=["PUT"])
    def update_supervisors(employee_user):
        try:
            supervisor = Supervisor.json_parse(request.json)
            supervisor.employee_user = employee_user
            SupervisorService.update_supervisor(supervisor)
            return jsonify(supervisor.json()), 200
        except KeyError:
            return "Please enter a new Supervisor for this Employee", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/supervisors/<employee_user>")
    def delete_supervisor(employee_user):
        try:
            return SupervisorService.delete_supervisor(employee_user)
        except KeyError:
            return "Supervisor or Employee not found.", 400
