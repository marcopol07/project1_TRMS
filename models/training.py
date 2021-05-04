class Training:
    def __init__(self, case_id=0, employee_user="", tuition_type="", date_submitted=0, training_date=0,
                 ds_approval=False, dh_approval=False, benco_approval=False, final_grade="", justification="",
                 reimbursement_amount=0):
        self.case_id = case_id
        self.employee_user = employee_user
        self.tuition_type = tuition_type
        self.date_submitted = date_submitted
        self.training_date = training_date
        self.ds_approval = ds_approval
        self.dh_approval = dh_approval
        self.benco_approval = benco_approval
        self.final_grade = final_grade
        self.justification = justification
        self.reimbursement_amount = reimbursement_amount
        self.query = None
        self.answer = None

    def json(self):
        return {
            "caseId": self.case_id,
            "employeeUser": self.employee_user,
            "tuitionType": self.tuition_type,
            "dateSubmitted": self.date_submitted,
            "trainingDate": self.training_date,
            "dsApproval": self.ds_approval,
            "dhApproval": self.dh_approval,
            "bencoApproval": self.benco_approval,
            "finalGrade": self.final_grade,
            "justification": self.justification,
            "reimbursementAmount": self.reimbursement_amount,
            "query": self.query,
            "answer": self.answer
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        training = Training()
        training.case_id = json["caseId"] if "caseId" in json else ""
        training.employee_user = json["employeeUser"] if "employeeUser" in json else ""
        training.tuition_type = json["tuitionType"]
        training.date_submitted = json["dateSubmitted"]
        training.training_date = json["trainingDate"] if "trainingDate" in json else 0
        training.ds_approval = json["dsApproval"] if "dsApproval" in json else False
        training.dh_approval = json["dhApproval"] if "dhApproval" in json else False
        training.benco_approval = json["bencoApproval"] if "bencoApproval" in json else False
        training.final_grade = json["finalGrade"] if "finalGrade" in json else ""
        training.justification = json["justification"] if "justification" in json else ""
        training.reimbursement_amount = json["reimbursementAmount"] if "reimbursementAmount" in json else 0
        training.query = json["query"] if "query" in json else None
        training.answer = json["answer"] if "answer" in json else None
        return training
