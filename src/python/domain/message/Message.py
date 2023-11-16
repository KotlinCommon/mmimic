from enum import Enum


class Message(Enum):
    # Messages related to Events
    DirectMsgReceived = "Received your message:"

    # Messages related to GeneralCommands
    DiceRollInvalidSides = "The number of sides must be at least 1."
    DiceRollResult = "You rolled a {sides}-sided dice and got: {result}"

    # Messages related to FunCommands
    PingResponse = "Pong!"

    def __str__(self):
        return self.value

    @staticmethod
    def format_dice_roll_result(sides, result):
        """Formats the dice roll result message."""
        return Message.DiceRollResult.value.format(sides=sides, result=result)
