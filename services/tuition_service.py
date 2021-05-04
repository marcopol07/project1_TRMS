from daos.tuition_dao import TuitionDAO
from exceptions.cannot_create_new import CannotCreateNew
from exceptions.resource_not_found import ResourceNotFound


class TuitionService:
    tuition_dao = TuitionDAO()

    @classmethod
    def add_tuition_type(cls, tuition):
        try:
            cls.tuition_dao.get_record(tuition.tuition_name)
            raise CannotCreateNew(f"That tuition already exists.")
        except ResourceNotFound:
            return cls.tuition_dao.create_record(tuition)

    @classmethod
    def get_all_tuitions(cls):
        return cls.tuition_dao.get_all_records()

    @classmethod
    def get_tuition(cls, tuition_name):
        return cls.tuition_dao.get_record(tuition_name)

    @classmethod
    def update_tuition(cls, change):
        try:
            cls.tuition_dao.get_record(change.tuition_name)
            return cls.tuition_dao.update_record(change)
        except ResourceNotFound as r:
            return r.message, 404

    @classmethod
    def delete_tuition(cls, tuition_name):
        try:
            cls.tuition_dao.get_record(tuition_name)
            return cls.tuition_dao.delete_record(tuition_name)
        except ResourceNotFound as r:
            return r.message, 404
