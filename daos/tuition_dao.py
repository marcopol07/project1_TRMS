from daos.model_dao import ModelDAO
from db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.tuition_type import TuitionType


class TuitionDAO(ModelDAO):
    def create_record(self, tuition, fk1=None, fk2=None):
        sql = "INSERT INTO tuition_types (%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (tuition.tuition_name, tuition.grading_format,
                             tuition.grade_cutoff, tuition.reimbursement_percent))
        connection.commit()
        record = cursor.fetchone()
        return TuitionType(record[0], record[1], record[2], record[3])

    def get_all_records(self):
        sql = "SELECT * FROM tuition_types"
        cursor = connection.cursor
        cursor.execute(sql)
        records = cursor.fetchall()

        tuitions_list = []
        for record in records:
            tuition = TuitionType(record[0], record[1], record[2], record[3])
            tuitions_list.append(tuition)

        return tuitions_list

    def get_record(self, tuition_name, fk1=None, fk2=None):
        sql = "SELECT * FROM tuition_types WHERE tuition_name=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [tuition_name])

        record = cursor.fetchone()

        if record:
            return TuitionType(record[0], record[1], record[2], record[3])
        else:
            raise ResourceNotFound(f"Tuition by name {tuition_name} not found.")

    def update_record(self, change):
        sql = "UPDATE tuition_types SET grading_format=%s, grade_cutoff=%s, reimbursement_percent=%s " \
              "WHERE tuition_name=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.grading_format, change.grade_cutoff,
                             change.reimbursement_percent, change.tuition_name))
        connection.commit()

        return ""

    def delete_record(self, tuition_name):
        sql = "DELETE FROM tuition_types WHERE tuition_name=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [tuition_name])
        connection.commit()

        return ""
