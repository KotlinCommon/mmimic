from enum import Enum


class EndPoint(Enum):
    SignInBot = "/signInBot"
    SignUp = "/signUp"

    @staticmethod
    def userWithDiscordId(discordId):
        return f"/user/{discordId}"

    def __str__(self):
        return self.value
