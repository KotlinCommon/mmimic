from enum import Enum


class EndPoint(Enum):
    SignInBot = "/signInBot"
    SignUp = "/signUp"

    def __str__(self):
        return self.value
