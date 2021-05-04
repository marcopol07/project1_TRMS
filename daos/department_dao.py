from daos.model_dao import ModelDAO
from db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.department import Department


class DepartmentDAO(ModelDAO):
    def create_record(self, department, fk1=None, fk2=None):
        sql = "INSERT INTO departments VALUES (%s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (department.department_name, department.department_head))
        connection.commit()
        record = cursor.fetchone()
        return Department(record[0], record[1])

    def get_all_records(self):
        sql = "SELECT * FROM departments"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        department_list = []
        for record in records:
            department = Department(record[0], record[1])
            department_list.append(department.json())

        return department_list

    def get_record(self, department_name, fk1=None, fk2=None):
        sql = "SELECT * FROM departments WHERE department_name=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [department_name])

        record = cursor.fetchone()

        if record:
            return Department(record[0], record[1])
        else:
            raise ResourceNotFound(f"Department with name {department_name} not found.")

    def update_record(self, change):
        sql = "UPDATE departments SET department_head=%s WHERE department_name=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.department_head, change.department_name))
        connection.commit()

        return ""

    def delete_record(self, department_name):
        sql = "DELETE FROM departments WHERE department_name=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [department_name])
        connection.commit()

        return ""
