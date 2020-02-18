from abc import ABC, abstractmethod

class WorkItemAbst(ABC):

    def __init__(self):
        self.__index = -1

    @property
    def _index(self):
        return self.__index

    @_index.setter
    def _index(self, index):
        self.__index = index

    @abstractmethod
    def do_work(self):
        pass