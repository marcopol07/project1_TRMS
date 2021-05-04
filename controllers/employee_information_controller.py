from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.employee_information import EmployeeInformation
from services.employee_information_service import EmployeeInformationService


def route(app):
    @app.route("/employees/information", methods=["POST"])
    def post_employee_information():
        try:
            employee = EmployeeInformation.json_parse(request.json)
            employee = EmployeeInformationService.add_employee_information(employee)
            return jsonify(employee.json()), 201
        except KeyError:
            return "Please fill out all the information correctly.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/information", methods=["GET"])
    def get_all_employee_information():
        return EmployeeInformationService.get_all_employee_information()

    @app.route("/employees/information/<password>", methods=["GET"])
    def get_employee_information(password):
        try:
            employee = EmployeeInformationService.get_employee_information(password)
            return jsonify(employee.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/information/<password>", methods=["PUT"])
    def put_employee_information(password):
        try:
            employee = EmployeeInformation.json_parse(request.json)
            employee.password = password
            EmployeeInformationService.update_information(password)
            return jsonify(employee.json()), 200
        except KeyError:
            return "KeyError", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/information/<password>", methods=["DELETE"])
    def delete_employee_information(password):
        try:
            return EmployeeInformationService.delete_employee_information(password)
        except KeyError:
            return f"No account with those credentials found."
