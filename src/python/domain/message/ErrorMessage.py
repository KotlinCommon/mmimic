from enum import Enum


class ErrorMessage(Enum):

    def __str__(self):
        return self.value
