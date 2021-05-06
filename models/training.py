class Training:
    def __init__(self, case_id=0, employee_user="", tuition_type="", date_submitted=None, training_date=None,
                 direct_supervisor="", ds_approval=False, department_head="", dh_approval=False, benco_approval=False,
                 final_grade="", justification="", reimbursement_amount=0, query=None, query_whom=None, answer=None):
        self.case_id = case_id
        self.employee_user = employee_user
        self.tuition_type = tuition_type
        self.date_submitted = date_submitted
        self.training_date = training_date
        self.direct_supervisor = direct_supervisor
        self.ds_approval = ds_approval
        self.department_head = department_head
        self.dh_approval = dh_approval
        self.benco_approval = benco_approval
        self.final_grade = final_grade
        self.justification = justification
        self.reimbursement_amount = reimbursement_amount
        self.query = query
        self.query_whom = query_whom
        self.answer = answer

    def json(self):
        return {
            "caseId": self.case_id,
            "employeeUser": self.employee_user,
            "tuitionType": self.tuition_type,
            "dateSubmitted": self.date_submitted,
            "trainingDate": self.training_date,
            "directSupervisor": self.direct_supervisor,
            "dsApproval": self.ds_approval,
            "departmentHead": self.department_head,
            "dhApproval": self.dh_approval,
            "bencoApproval": self.benco_approval,
            "finalGrade": self.final_grade,
            "justification": self.justification,
            "reimbursementAmount": float(self.reimbursement_amount),
            "query": self.query,
            "queryWhom": self.query_whom,
            "answer": self.answer
        }

    def __repr__(self):
        return str(self.json())

    @staticmethod
    def json_parse(json):
        training = Training()
        training.case_id = json["caseId"] if "caseId" in json else ""
        training.employee_user = json["employeeUser"] if "employeeUser" in json else ""
        training.tuition_type = json["tuitionType"] if "tuitionType" in json else None
        training.date_submitted = json["dateSubmitted"] if "dateSubmitted" in json else None
        training.training_date = json["trainingDate"] if "trainingDate" in json else None
        training.direct_supervisor = json["directSupervisor"] if "directSupervisor" in json else ""
        training.ds_approval = json["dsApproval"] if "dsApproval" in json else False
        training.department_head = json["departmentHead"] if "departmentHead" in json else ""
        training.dh_approval = json["dhApproval"] if "dhApproval" in json else False
        training.benco_approval = json["bencoApproval"] if "bencoApproval" in json else False
        training.final_grade = json["finalGrade"] if "finalGrade" in json else ""
        training.justification = json["justification"] if "justification" in json else ""
        training.reimbursement_amount = json["reimbursementAmount"] if "reimbursementAmount" in json else 0
        training.query = json["query"] if "query" in json else None
        training.query_whom = json["queryWhom"] if "queryWhom" in json else None
        training.answer = json["answer"] if "answer" in json else None
        return training
