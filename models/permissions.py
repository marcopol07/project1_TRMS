class Permissions:
    def __init__(self, position_name="", department_head_access=False, ben_co_access=False):
        self.position_name = position_name
        self.department_head_access = department_head_access
        self.ben_co_access = ben_co_access

    def json(self):
        return {
            "positionName": self.position_name,
            "departmentHeadAccess": self.department_head_access,
            "benCoAccess": self.ben_co_access
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        permissions = Permissions()
        permissions.position_name = json["positionName"]
        permissions.department_head_access = json["departmentHeadAccess"] if "departmentHeadAccess" in json else False
        permissions.ben_co_access = json["benCoAccess"] if "benCoAccess" in json else False
        return permissions
