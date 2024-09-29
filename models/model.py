from abc import ABC, abstractmethod

class Model(ABC):

    @staticmethod
    @abstractmethod
    def generate() -> list:
        pass