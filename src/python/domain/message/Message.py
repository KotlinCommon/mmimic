from enum import Enum


class Message(Enum):
    Error = "An error occurred:"
    InProduction = "In production"
    AllowedServer = "I'm only allowed in the specific server!"

    # Messages related to FunCommands
    PingResponse = "Pong!"

    def __str__(self):
        return self.value

    @staticmethod
    def formatError(inputContent):
        """Formats the invalid input message."""
        return Message.Error.value.format(input=inputContent)
