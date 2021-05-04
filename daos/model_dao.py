from abc import ABC, abstractmethod


class ModelDAO(ABC):
    @abstractmethod
    def create_record(self, record, fk1, fk2):
        pass

    @abstractmethod
    def get_all_records(self):
        pass

    @abstractmethod
    def get_record(self, pk, fk1, fk2):
        pass

    @abstractmethod
    def update_record(self, change):
        pass

    @abstractmethod
    def delete_record(self, pk):
        pass
