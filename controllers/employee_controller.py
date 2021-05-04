from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from services.employee_service import EmployeeService


def route(app):
    @app.route("/employees", methods=["POST"])
    def post_employee():
        try:
            employee = Employee.json_parse(request.json)
            employee = EmployeeService.add_employee(employee)
            return jsonify(employee.json()), 201
        except KeyError:
            return "Please enter a username.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees", methods=["GET"])
    def get_all_employees():
        return jsonify(EmployeeService.get_all_employees())

    @app.route("/employees/<username>", methods=["GET"])
    def get_employee(username):
        try:
            employee = EmployeeService.get_employee(username)
            return jsonify(employee.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees", methods=["DELETE"])
    def delete_employee(username):
        try:
            return EmployeeService.delete_employee(username)
        except KeyError:
            return "No Employee found by that username.", 400
