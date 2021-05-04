from daos.employee_dao import EmployeeDAO
from daos.supervisors_dao import SupervisorDAO
from exceptions.resource_not_found import ResourceNotFound


class SupervisorService:
    supervisor_dao = SupervisorDAO()
    employee_dao = EmployeeDAO()

    @classmethod
    def add_supervisor(cls, supervisor):
        cls.employee_dao.get_record(supervisor.employee_user)
        cls.employee_dao.get_record(supervisor.supervisor_user)
        return cls.supervisor_dao.create_record(supervisor)

    @classmethod
    def get_all_supervisors(cls):
        return cls.supervisor_dao.get_all_records()

    @classmethod
    def get_supervisor(cls, employee_user):
        return cls.supervisor_dao.get_record(employee_user)

    @classmethod
    def update_supervisor(cls, change):
        try:
            cls.employee_dao.get_record(change.employee_user)
            cls.employee_dao.get_record(change.supervisor_user)
            return cls.supervisor_dao.update_record(change)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def delete_supervisor(cls, employee_user):
        try:
            cls.employee_dao.get_record(employee_user)
            return cls.supervisor_dao.delete_record(employee_user), 204
        except ResourceNotFound as r:
            return r.message, 404
