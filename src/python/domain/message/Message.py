from enum import Enum


class Message(Enum):
    Error = "An error occurred:"

    @staticmethod
    def formatError(inputContent):
        """Formats the invalid input message."""
        return Message.Error.value.format(input=inputContent)

    InProduction = "In production"
    AllowedServer = "I'm only allowed in the specific server!"

    # Messages related to FunCommands
    PingResponse = "Pong!"

    # Messages related to GPT :
    GTPSorry = "Sorry, I can't process your request right now."

    # Messages related to Adventure
    AdventureProcessing = "Processing your adventure... ⏳"
    AdventureCommandCannot = "This command cannot be used in direct messages."
    AdventureSessionAlready = "An adventure session is already active in this channel."
    AdventureCannotUsed = "This command cannot be used in direct messages."
    AdventureNotStarted = "You are not the one who started this adventure session."
    AdventureStarted = "Adventure session started for {} in this channel.\n\n"
    AdventureEnded = "Adventure session ended for {} in this channel."

    @staticmethod
    def formatAdventureStarted(authorMention):
        return Message.AdventureStarted.value.format(authorMention)

    @staticmethod
    def formatAdventureEnded(authorMention):
        return Message.AdventureEnded.value.format(authorMention)

    def __str__(self):
        return self.value
