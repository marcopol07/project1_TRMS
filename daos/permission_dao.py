from daos.model_dao import ModelDAO
from db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.permissions import Permissions


class PermissionDAO(ModelDAO):
    def create_record(self, permission, fk1=None, fk2=None):
        sql = "INSERT INTO permissions VALUES (%s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (permission.position_name, permission.department_head_access, permission.ben_co_access))
        connection.commit()
        record = cursor.fetchone()
        return Permissions(record[0], record[1], record[2])

    def get_all_records(self):
        sql = "SELECT * FROM permissions"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        permission_list = []
        for record in records:
            permission = Permissions(record[0], record[1], record[2])
            permission_list.append(permission.json())

        return permission_list

    def get_record(self, position_name, fk1=None, fk2=None):
        sql = "SELECT * FROM permissions WHERE position_name=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [position_name])

        record = cursor.fetchone()

        if record:
            return Permissions(record[0], record[1], record[2])
        else:
            raise ResourceNotFound(f"Permissions for position {position_name} not found.")

    def update_record(self, change):
        sql = "UPDATE permissions SET department_head_access=%s, ben_co_access=%s WHERE position_name=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.department_head_access, change.ben_co_access, change.position_name))
        connection.commit()

        return ""

    def delete_record(self, position_name):
        sql = "DELETE FROM permissions WHERE position_name=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [position_name])
        connection.commit()

        return ""
