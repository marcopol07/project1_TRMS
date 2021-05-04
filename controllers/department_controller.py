from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.department import Department
from services.department_service import DepartmentService


def route(app):
    @app.route("/departments", methods=["POST"])
    def post_department():
        try:
            department = Department.json_parse(request.json)
            department = DepartmentService.add_department(department)
            return jsonify(department.json()), 201
        except KeyError:
            return "A name and department head must be entered to add a department.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/departments", methods=["GET"])
    def get_all_departments():
        return jsonify(DepartmentService.get_all_departments())

    @app.route("/departments/<department_name>", methods=["GET"])
    def get_department(department_name):
        try:
            department = DepartmentService.get_department(department_name)
            return jsonify(department.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/departments/<department_name>", methods=["PUT"])
    def update_department(department_name):
        try:
            department = Department.json_parse(request.json)
            department.department_name = department_name
            DepartmentService.update_department(department)
            return jsonify(department.json()), 200
        except KeyError:
            return "Please enter a new Department Head for this Department.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/departments/<department_name>", methods=["DELETE"])
    def delete_department(department_name):
        try:
            return DepartmentService.delete_department(department_name)
        except KeyError:
            return f"No Department with name {department_name} found.", 400
