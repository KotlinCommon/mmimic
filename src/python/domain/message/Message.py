from enum import Enum


class Message(Enum):
    Error = "An error occurred:"
    InProduction = "In production"

    # Messages related to Events
    DirectMsgReceived = "Received your message:"

    # Messages related to GeneralCommands
    DiceRollInvalidSides = "The number of sides must be at least 1."
    DiceRollResult = "You rolled a {sides}-sided dice and got: {result}"

    # Messages related to FunCommands
    PingResponse = "Pong!"

    # Messages related to signUp User
    RegistrationComplete = "Registration complete. Thank you!"
    AlreadyRegistered = "You are already registered"

    # Messages related to Direct
    CanIHelpYou = "how can I help you ?"
    ForRegister = "for register send : register"
    TookLongToRespond = "You took too long to respond."
    InvalidInput = "Invalid input: {input}. Please try again."

    def __str__(self):
        return self.value

    @staticmethod
    def formatError(inputContent):
        """Formats the invalid input message."""
        return Message.Error.value.format(input=inputContent)

    @staticmethod
    def formatDiceRollResult(sides, result):
        """Formats the dice roll result message."""
        return Message.DiceRollResult.value.format(sides=sides, result=result)

    @staticmethod
    def formatInvalidInput(inputContent):
        """Formats the invalid input message."""
        return Message.InvalidInput.value.format(input=inputContent)
