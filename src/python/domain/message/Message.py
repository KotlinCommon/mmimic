from enum import Enum


class Message(Enum):
    Error = "An error occurred:"
    InProduction = "In production"
    AllowedServer = "I'm only allowed in the specific server!"

    # Messages related to FunCommands
    PingResponse = "Pong!"

    # Messages related to Events
    AdventureNotActive = "You do not have an active story session in this channel."
    AdventureStarted = " has started a new story session."
    AdventureEnd = "Your story session has ended."
    AdventureAlreadyActive = "A Adventure session is already active in this channel."

    def __str__(self):
        return self.value

    @staticmethod
    def formatError(inputContent):
        """Formats the invalid input message."""
        return Message.Error.value.format(input=inputContent)
