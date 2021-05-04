from daos.employee_dao import EmployeeDAO
from exceptions.cannot_create_new import CannotCreateNew
from exceptions.resource_not_found import ResourceNotFound


class EmployeeService:
    employee_dao = EmployeeDAO()

    @classmethod
    def add_employee(cls, employee):
        try:
            cls.employee_dao.get_record(employee.username)
            raise CannotCreateNew(f"That username already exists! Try another one.")
        except ResourceNotFound:
            return cls.employee_dao.create_record(employee)

    @classmethod
    def get_all_employees(cls):
        return cls.employee_dao.get_all_records()

    @classmethod
    def get_employee(cls, username):
        return cls.employee_dao.get_record(username)

    @classmethod
    def delete_employee(cls, username):
        return cls.employee_dao.delete_record(username)
