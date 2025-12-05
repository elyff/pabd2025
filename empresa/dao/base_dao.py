from abc import ABC, abstractmethod

class BaseDAO(ABC):
    @abstractmethod
    def create(self, obj): pass
    @abstractmethod
    def read(self, id_): pass
    @abstractmethod
    def update(self, obj): pass
    @abstractmethod
    def delete(self, id_): pass
     