from daos.department_dao import DepartmentDAO
from daos.employee_dao import EmployeeDAO
from daos.employee_information_dao import EmployeeInformationDAO
from daos.supervisors_dao import SupervisorDAO
from daos.training_dao import TrainingDAO
from daos.tuition_dao import TuitionDAO
from exceptions.resource_not_found import ResourceNotFound


class TrainingService:
    employee_dao = EmployeeDAO()
    employee_information_dao = EmployeeInformationDAO()
    department_dao = DepartmentDAO()
    supervisor_dao = SupervisorDAO()
    tuition_dao = TuitionDAO()
    training_dao = TrainingDAO()

    @classmethod
    def create_training(cls, training, department_name):
        cls.employee_dao.get_record(training.employee_user)
        cls.tuition_dao.get_record(training.tuition_type)
        supervisor = cls.supervisor_dao.get_record(training.employee_user)
        department = cls.department_dao.get_record(department_name)
        training.direct_supervisor = supervisor.supervisor_user
        training.department_head = department.department_head
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
    def update_approvals(cls, case_id, level):
        try:
            cls.training_dao.get_record(case_id)
            return cls.training_dao.update_approval(case_id, level)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def update_reimbursement_amount(cls, case_id, password, value, add="add"):
        try:
            cls.training_dao.get_record(case_id)
            employee = cls.employee_information_dao.get_record(password)
            if add == "add":
                new_funds = value + employee.reimbursement_funds_remaining
            elif employee.reimbursement_funds_remaining < value:
                value = employee.reimbursement_funds_remaining
                new_funds = 0
            else:
                new_funds = employee.reimbursement_funds_remaining - value
            cls.employee_information_dao.update_reimbursement(password, new_funds)
            return cls.training_dao.update_reimbursement_amount(case_id, value)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def update_query(cls, change):
        return cls.training_dao.update_query(change)

    @classmethod
    def delete_training(cls, case_id):
        try:
            cls.training_dao.get_record(case_id)
            return cls.training_dao.delete_record(case_id)
        except ResourceNotFound as r:
            return r.message, 404
