import json


class EmployeeInformation:
    def __init__(self, last_name="", first_name="", username="", password="", dob=None,
                 department="", position_name="", reimbursement_funds_remaining=0):
        self.last_name = last_name
        self.first_name = first_name
        self.username = username
        self.password = password
        self.dob = dob
        self.department = department
        self.position_name = position_name
        self.reimbursement_funds_remaining = float(reimbursement_funds_remaining)

    def json(self):
        return {
            "lastName": self.last_name,
            "firstName": self.first_name,
            "username": self.username,
            "password": self.password,
            "dob": self.dob,
            "department": self.department,
            "positionName": self.position_name,
            "reimbursementFundsRemaining": float(self.reimbursement_funds_remaining)
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        employee = EmployeeInformation()
        employee.last_name = json["lastName"] if "lastName" in json else ""
        employee.first_name = json["firstName"] if "firstName" in json else ""
        employee.username = json["username"]
        employee.password = json["password"]
        employee.dob = json["dob"] if "dob" in json else None
        employee.department = json["department"] if "department" in json else ""
        employee.position_name = json["positionName"] if "positionName" in json else ""
        employee.reimbursement_funds_remaining = json[
            "reimbursementFundsRemaining"] if "reimbursementFundsRemaining" in json else 0
        return employee
