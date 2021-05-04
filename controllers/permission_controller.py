from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.permissions import Permissions
from services.permission_service import PermissionService


def route(app):
    @app.route("/permissions", methods=["POST"])
    def post_permission():
        try:
            permission = Permissions.json_parse(request.json)
            permission = PermissionService.add_permission(permission)
            return jsonify(permission.json()), 201
        except KeyError:
            return "Please enter a position.", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/permissions", methods=["GET"])
    def get_all_permissions():
        return jsonify(PermissionService.get_all_permissions())

    @app.route("/permissions/<position_name>", methods=["GET"])
    def get_permission(position_name):
        try:
            permission = PermissionService.get_permission(position_name)
            return jsonify(permission.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/permissions/<position_name>", methods=["DELETE"])
    def delete_permission(position_name):
        try:
            return PermissionService.delete_permission(position_name)
        except KeyError:
            return "No Permissions found for that position.", 400