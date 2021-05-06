from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.training import Training
from services.training_service import TrainingService


def route(app):
    @app.route("/trainings", methods=["POST"])
    def post_training():
        try:
            department_name = request.json["department"]
            training = Training.json_parse(request.json)
            training = TrainingService.create_training(training, department_name)
            return jsonify(training.json()), 201
        except KeyError:
            return "Please fill out all required fields.", 400

    @app.route("/trainings", methods=["GET"])
    def get_all_trainings():
        return jsonify(TrainingService.get_all_trainings())

    @app.route("/trainings/<employee_user>", methods=["GET"])
    def get_trainings_for_employee(employee_user):
        try:
            return jsonify(TrainingService.get_all_employee_trainings(employee_user)), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/trainings/<case_id>", methods=["GET"])
    def get_training(case_id):
        try:
            training = TrainingService.get_training(case_id)
            return jsonify(training.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/trainings/<case_id>", methods=["PUT"])
    def update_training(case_id):
        try:
            training = Training.json_parse(request.json)
            training.case_id = case_id
            TrainingService.update_training(training)
            return jsonify(training.json()), 200
        except KeyError:
            return "Please enter correct information.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/trainings/<case_id>/<level>", methods=["PUT"])
    def update_approvals(case_id, level):
        return TrainingService.update_approvals(case_id, level), 200

    @app.route("/trainings/<case_id>/<value>/<add>", methods=["PUT"])
    def update_reimbursements(case_id, value, add):
        return TrainingService.update_reimbursement_amount(case_id, value, add), 200

    @app.route("/trainings/query/<case_id>", methods=["PUT"])
    def update_query(case_id):
        training = Training.json_parse(request.json)
        training.case_id = case_id
        return TrainingService.update_query(training), 200

    @app.route("/trainings/<case_id>", methods=["DELETE"])
    def delete_training(case_id):
        try:
            return TrainingService.delete_training(case_id), 204
        except KeyError:
            return "No training found.", 400
