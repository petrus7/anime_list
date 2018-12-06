import abc

class Validator(abc.ABC):

    def __init__(self, validation_string):
        self.data = validation_string

    @abc.abstractmethod
    def validate(self):
        pass
