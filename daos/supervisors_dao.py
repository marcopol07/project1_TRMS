from daos.model_dao import ModelDAO
from db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.supervisor import Supervisor


class SupervisorDAO(ModelDAO):
    def create_record(self, supervisor, fk1=None, fk2=None):
        sql = "INSERT INTO supervisors VALUES (DEFAULT, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (supervisor.employee_user, supervisor.supervisor_user))
        connection.commit()
        record = cursor.fetchone()
        return Supervisor(record[0], record[1], record[2])

    def get_all_records(self):
        sql = "SELECT * FROM supervisors"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        supervisor_list = []
        for record in records:
            supervisor = Supervisor(record[0], record[1], record[2])
            supervisor_list.append(supervisor.json())

        return supervisor_list

    def get_record(self, employee_user, fk1=None, fk2=None):
        sql = "SELECT * FROM supervisors WHERE employee_user=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_user])

        record = cursor.fetchone()

        if record:
            return Supervisor(record[0], record[1], record[2])
        else:
            raise ResourceNotFound(f"No record found for user {employee_user}")

    def update_record(self, change):
        sql = "UPDATE supervisors SET supervisor_user=%s WHERE employee_user=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.supervisor_user, change.employee_user))
        connection.commit()

        return ""

    def delete_record(self, employee_user):
        sql = "DELETE FROM supervisors WHERE employee_user=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_user])
        connection.commit()

        return ""
