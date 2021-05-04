from daos.model_dao import ModelDAO
from db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee


class EmployeeDAO(ModelDAO):
    def create_record(self, employee, fk1=None, fk2=None):
        sql = "INSERT INTO employees VALUES (%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [employee.username])
        connection.commit()
        record = cursor.fetchone()
        return Employee(record[0])

    def get_all_records(self):
        sql = "SELECT * FROM employees"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        employee_list = []
        for record in records:
            employee = Employee(record[0])
            employee_list.append(employee.json())

        return employee_list

    def get_record(self, username, fk1=None, fk2=None):
        sql = "SELECT * FROM employees WHERE username=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])

        record = cursor.fetchone()

        if record:
            return Employee(record[0])
        else:
            raise ResourceNotFound(f"Employee with user {username} not found.")

    def update_record(self, change=None):
        pass

    def delete_record(self, username):
        sql = "DELETE FROM employees WHERE username=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [username])
        connection.commit()

        return ""
