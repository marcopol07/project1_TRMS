from daos.department_dao import DepartmentDAO
from daos.employee_dao import EmployeeDAO
from daos.employee_information_dao import EmployeeInformationDAO
from daos.permission_dao import PermissionDAO
from exceptions.cannot_create_new import CannotCreateNew
from exceptions.resource_not_found import ResourceNotFound


class EmployeeInformationService:
    employee_dao = EmployeeDAO()
    department_dao = DepartmentDAO()
    permission_dao = PermissionDAO()
    ei_dao = EmployeeInformationDAO()

    @classmethod
    def add_employee_information(cls, employee):
        try:
            cls.ei_dao.get_record(employee.password)
            raise CannotCreateNew("A user already has that password.")
        except ResourceNotFound:
            cls.employee_dao.get_record(employee.username)
            cls.department_dao.get_record(employee.department)
            cls.permission_dao.get_record(employee.position_name)
            return cls.ei_dao.create_record(employee)

    @classmethod
    def get_all_employee_information(cls):
        return  cls.ei_dao.get_all_records()

    @classmethod
    def get_employee_information(cls, password):
        return cls.ei_dao.get_record(password)

    @classmethod
    def update_information(cls, change):
        try:
            cls.ei_dao.get_record(change.password)
            cls.employee_dao.get_record(change.username)
            cls.department_dao.get_record(change.department_name)
            cls.permission_dao.get_record(change.position_name)
            return cls.ei_dao.update_record(change)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def delete_employee_information(cls, password):
        try:
            cls.ei_dao.get_record(password)
            return cls.ei_dao.delete_record(password), 204
        except ResourceNotFound as r:
            return r.message, 404
