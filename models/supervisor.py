class Supervisor:
    def __init__(self, case_id=0, employee_user="", supervisor_user=""):
        self.case_id = case_id
        self.employee_user = employee_user
        self.supervisor_user = supervisor_user

    def json(self):
        return {
            "caseId": self.case_id,
            "employeeUser": self.employee_user,
            "supervisorUser": self.supervisor_user,
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        supervisor = Supervisor()
        supervisor.case_id = json["caseId"] if "caseId" in json else 0
        supervisor.employee_user = json["employeeUser"] if "employeeUser" in json else ""
        supervisor.supervisor_user = json["supervisorUser"] if "supervisorUser" in json else ""
        return supervisor
