class TuitionType:
    def __init__(self, tuition_name="", grading_format=False, grade_cutoff=None, reimbursement_percent=0):
        self.tuition_name = tuition_name
        self.grading_format = grading_format
        self.grade_cutoff = grade_cutoff
        self.reimbursement_percent = reimbursement_percent

    def json(self):
        return {
            "tuitionName": self.tuition_name,
            "gradingFormat": self.grading_format,
            "gradeCutoff": self.grade_cutoff,
            "reimbursementPercent": float(self.reimbursement_percent)
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        tuition_type = TuitionType()
        tuition_type.tuition_name = json["tuitionName"]
        tuition_type.grading_format = json["gradingFormat"] if "gradingFormat" in json else False
        tuition_type.grade_cutoff = json["gradeCutoff"] if "gradeCutoff" in json else ""
        tuition_type.reimbursement_percent = json["reimbursementPercent"] if "reimbursementPercent" in json else 0
        return tuition_type
