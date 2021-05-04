from daos.employee_dao import EmployeeDAO
from daos.training_dao import TrainingDAO
from daos.tuition_dao import TuitionDAO
from exceptions.resource_not_found import ResourceNotFound


class TrainingService:
    employee_dao = EmployeeDAO()
    tuition_dao = TuitionDAO()
    training_dao = TrainingDAO()

    @classmethod
    def create_training(cls, training):
        cls.employee_dao.get_record(training.employee_user)
        cls.tuition_dao.get_record(training.tuition_type)
        return cls.training_dao.create_record(training)

    @classmethod
    def get_all_trainings(cls):
        return cls.training_dao.get_all_records()

    @classmethod
    def get_all_employee_trainings(cls, employee_user):
        cls.employee_dao.get_record(employee_user)
        return cls.training_dao.get_records_by_employee(employee_user)

    @classmethod
    def get_training(cls, case_id):
        return cls.training_dao.get_record(case_id)

    @classmethod
    def update_training(cls, change):
        try:
            cls.training_dao.get_record(change.case_id)
            return cls.training_dao.update_record(change)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def delete_training(cls, case_id):
        try:
            cls.training_dao.get_record(case_id)
            return cls.training_dao.delete_record(case_id)
        except ResourceNotFound as r:
            return r.message, 404
