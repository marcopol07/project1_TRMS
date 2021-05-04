from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.tuition_type import TuitionType
from services.tuition_service import TuitionService


def route(app):
    @app.route("/tuitions", methods=["POST"])
    def post_tuition():
        try:
            tuition = TuitionType.json_parse(request.json)
            tuition = TuitionService.add_tuition_type(tuition)
            return jsonify(tuition.json()), 201
        except KeyError:
            return "Please enter a proper Tuition Type.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/tuitions", methods=["GET"])
    def get_all_tuitions():
        return jsonify(TuitionService.get_all_tuitions())

    @app.route("/tuitions/<tuition_name>", methods=["GET"])
    def get_tuition(tuition_name):
        try:
            tuition = TuitionService.get_tuition(tuition_name)
            return jsonify(tuition.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/tuitions/<tuition_name>", methods=["PUT"])
    def update_tuition(tuition_name):
        try:
            tuition = TuitionType.json_parse(request.json)
            tuition.tuition_name = tuition_name
            TuitionService.update_tuition(tuition)
            return jsonify(tuition.json())
        except KeyError:
            return f"Please enter valid data to update this Tuition", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/tuitions/<tuition_name>", methods=["DELETE"])
    def delete_tuition(tuition_name):
        try:
            return TuitionService.delete_tuition(tuition_name)
        except KeyError:
            return "Please enter a proper Tuition Type.", 400
