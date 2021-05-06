from daos.model_dao import ModelDAO
from db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.training import Training


class TrainingDAO(ModelDAO):
    def create_record(self, training, fk1=None, fk2=None):
        sql = "INSERT INTO trainings VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (training.employee_user, training.tuition_type, training.date_submitted,
                             training.training_date, training.direct_supervisor, training.ds_approval,
                             training.department_head, training.dh_approval, training.benco_approval,
                             training.final_grade, training.justification, training.reimbursement_amount))
        connection.commit()
        record = cursor.fetchone()
        return Training(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                        record[8], record[9], record[10], record[11], record[12])

    def get_all_records(self):
        sql = "SELECT * FROM trainings"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        training_list = []
        for record in records:
            training = Training(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                                record[8], record[9], record[10], record[11], float(record[12]), record[13], record[14],
                                record[15])
            training_list.append(training.json())

        return training_list

    @staticmethod
    def get_records_by_employee(employee_user):
        sql = "SELECT * FROM trainings WHERE employee_user=%s"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        training_list = []
        for record in records:
            training = Training(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                                record[8], record[9], record[10], record[11], float(record[12]), record[13], record[14],
                                record[15])
            training_list.append(training.json())

        return training_list

    def get_record(self, case_id, fk1=None, fk2=None):
        sql = "SELECT * FROM trainings WHERE case_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [case_id])

        record = cursor.fetchone()

        if record:
            return Training(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                            record[8], record[9], record[10], record[11], float(record[12]), record[13], record[14],
                            record[15])
        else:
            raise ResourceNotFound("No submission found for that ID.")

    def update_record(self, change):
        sql = "UPDATE trainings SET ds_approval=%s, dh_approval=%s, benco_approval=%s, final_grade=%s, " \
              "reimbursement_amount=%s, query=%s, query_whom=%s, answer=%s WHERE case_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.ds_approval, change.dh_approval, change.benco_approval, change.final_grade,
                             change.reimbursement_amount, change.query, change.query_whom, change.answer,
                             change.case_id))
        connection.commit()

        return ""

    @staticmethod
    def update_approval(case_id, level):
        sql = "UPDATE trainings SET " + level + "=TRUE WHERE case_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [case_id])
        connection.commit()

        return ""

    @staticmethod
    def update_reimbursement_amount(case_id, value):
        sql = "UPDATE trainings SET reimbursement_amount=%s WHERE case_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (value, case_id))
        connection.commit()

        return ""

    @staticmethod
    def update_query(change):
        sql = "UPDATE trainings SET query=%s WHERE case_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.query, change.case_id))
        connection.commit()

        return ""

    def delete_record(self, case_id):
        sql = "DELETE FROM trainings WHERE case_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [case_id])
        connection.commit()

        return ""
