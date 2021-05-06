from daos.model_dao import ModelDAO
from db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.employee_information import EmployeeInformation


class EmployeeInformationDAO(ModelDAO):
    def create_record(self, employee, fk1=None, fk2=None):
        sql = "INSERT INTO employee_information VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql,
                       (employee.last_name, employee.first_name, employee.username, employee.password, employee.dob,
                        employee.department, employee.position_name, employee.reimbursement_funds_remaining))
        connection.commit()
        record = cursor.fetchone()
        return EmployeeInformation(record[0], record[1], record[2], record[3],
                                   record[4], record[5], record[6], record[7])

    def get_all_records(self):
        sql = "SELECT * FROM employee_information"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        employee_list = []
        for record in records:
            employee = EmployeeInformation(record[0], record[1], record[2], record[3],
                                           record[4], record[5], record[6], record[7])
            employee_list.append(employee.json())

        return employee_list

    def get_record(self, password, fk1=None, fk2=None):
        sql = "SELECT * FROM employee_information WHERE password=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [password])

        record = cursor.fetchone()

        if record:
            return EmployeeInformation(record[0], record[1], record[2], record[3],
                                       record[4], record[5], record[6], record[7])
        else:
            raise ResourceNotFound(f"Password does not match credentials in database.")

    def update_record(self, change):
        sql = "UPDATE employee_information SET last_name=%s,first_name=%s,dob=%s,department=%s," \
              "position_name=%s,reimbursement_funds_remaining=%s WHERE password=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.last_name, change.first_name, change.dob, change.department, change.position_name,
                             change.reimbursement_funds_remaining, change.password))
        connection.commit()

        return ""

    @staticmethod
    def update_reimbursement(self, password, change):
        sql = "UPDATE reimbursement_funds_remaining=%s WHERE password=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change, password))
        connection.commit()

        return ""

    def delete_record(self, password):
        sql = "DELETE FROM employee_information WHERE password=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [password])
        connection.commit()

        return ""
