from enum import Enum


class EndPoint(Enum):
    SignInBot = "/signInBot"

    def __str__(self):
        return self.value
