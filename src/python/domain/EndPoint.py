from enum import Enum


class EndPoint(Enum):
    SignInBot = "/signInBot"
    SignUp = "/signUp"
    character = "/character"

    @staticmethod
    def userWithDiscordId(discordId):
        return f"/user/{discordId}"

    @staticmethod
    def characterWithUserId(userId):
        return f"/character/{userId}"

    @staticmethod
    def charactersWithUserId(userId):
        return f"/characters/{userId}"

    def __str__(self):
        return self.value
