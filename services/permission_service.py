from daos.permission_dao import PermissionDAO
from exceptions.cannot_create_new import CannotCreateNew
from exceptions.resource_not_found import ResourceNotFound


class PermissionService:
    permission_dao = PermissionDAO()

    @classmethod
    def add_permission(cls, permission):
        try:
            cls.permission_dao.get_record(permission.position_name)
            raise CannotCreateNew(f"There is already a position called {permission.position_name}.")
        except ResourceNotFound as r:
            return cls.permission_dao.create_record(permission)

    @classmethod
    def get_all_permissions(cls):
        return cls.permission_dao.get_all_records()

    @classmethod
    def get_permission(cls, position_name):
        return cls.permission_dao.get_record(position_name)

    @classmethod
    def update_permission(cls, change):
        try:
            cls.permission_dao.get_record(change.position_name)
            return cls.permission_dao.update_record(change)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def delete_permission(cls, position_name):
        try:
            cls.permission_dao.get_record(position_name)
            return cls.permission_dao.delete_record(position_name), 204
        except ResourceNotFound as r:
            return r.message, 404
