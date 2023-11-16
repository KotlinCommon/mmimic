from enum import Enum


class ErrorMessage(Enum):
    TokenNotFound = "Authentication failed: Bearer token not found in response headers"
    AuthenticationFailed = "Authentication failed : "

    def __str__(self):
        return self.value
