from daos.department_dao import DepartmentDAO
from daos.employee_dao import EmployeeDAO
from exceptions.cannot_create_new import CannotCreateNew
from exceptions.resource_not_found import ResourceNotFound


class DepartmentService:
    department_dao = DepartmentDAO()
    employee_dao = EmployeeDAO()

    @classmethod
    def add_department(cls, department):
        try:
            cls.department_dao.get_record(department.department_name)
            raise CannotCreateNew(f"There is already a department by the name {department.department_name}.")
        except ResourceNotFound:
            cls.employee_dao.get_record(department.department_head)
            return cls.department_dao.create_record(department)

    @classmethod
    def get_all_departments(cls):
        return cls.department_dao.get_all_records()

    @classmethod
    def get_department(cls, department_name):
        return cls.department_dao.get_record(department_name)

    @classmethod
    def update_department(cls, change):
        try:
            cls.department_dao.get_record(change.department_name)
            cls.employee_dao.get_record(change.department_head)
            return cls.department_dao.update_record(change)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def delete_department(cls, department_name):
        try:
            cls.department_dao.get_record(department_name)
            return cls.department_dao.delete_record(department_name), 204
        except ResourceNotFound as r:
            return r.message, 404
