class Employee:
    def __init__(self, username=""):
        self.username = username

    def json(self):
        return {
            "username": self.username,
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        employee = Employee()
        employee.username = json["username"]

        return employee
