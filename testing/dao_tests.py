import unittest

from daos.employee_dao import EmployeeDAO
from daos.employee_information_dao import EmployeeInformationDAO
from daos.training_dao import TrainingDAO
from models.training import Training


class TestDAO(unittest.TestCase):
    training_dao = TrainingDAO()
    employee_dao = EmployeeDAO()
    employee_information_dao = EmployeeInformationDAO
    
    def test_create_new_form_success(self):
        training = Training()
        new_training = self.training_dao.create_record(training)
        self.assertEqual(isinstance(new_training, Training), True)

    def test_get_all_trainings_for_forms_success(self):
        trainings = self.training_dao.get_all_records()
        for training in trainings:
            if not isinstance(training, dict):
                raise AssertionError("Not every return is an Training object.")
        assert True

    def test_get_user_marc(self):
        employee = self.employee_dao.get_record("marc")
        self.assertEqual(employee.username, "marc")

    def test_get_password(self):
        employee = self.employee_information_dao.get_record('password')
        self.assertEqual(employee.username, "marc")



if __name__ == '__main__':
    unittest.main()
