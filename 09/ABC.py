from abc import ABCMeta
from abc import abstractmethod

class AbstractDuck(metaclass=ABCMeta):
    @abstractmethod
    def Kwak(self):
        pass

class Duck(AbstractDuck):
    pass

duck = Duck()