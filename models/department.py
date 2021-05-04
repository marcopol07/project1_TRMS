class Department:
    def __init__(self, department_name="", department_head=""):
        self.department_name = department_name
        self.department_head = department_head

    def json(self):
        return {
            "departmentName": self.department_name,
            "departmentHead": self.department_head
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        department = Department()
        department.department_name = json["departmentName"]
        # Think about returning head of company instead
        department.department_head = json["departmentHead"]
        return department
