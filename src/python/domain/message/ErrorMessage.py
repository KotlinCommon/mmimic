from enum import Enum


class ErrorMessage(Enum):

    # Messages related to Events
    TokenNotFound = "Token not found in response"


    def __str__(self):
        return self.value
