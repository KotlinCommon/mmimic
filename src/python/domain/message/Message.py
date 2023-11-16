from enum import Enum


class Message(Enum):
    # Messages related to Events
    DIRECT_MESSAGE_RECEIVED = "Received your message:"

    # Messages related to GeneralCommands
    DICE_ROLL_INVALID_SIDES = "The number of sides must be at least 1."
    DICE_ROLL_RESULT = "You rolled a {sides}-sided dice and got: {result}"

    # Messages related to FunCommands
    PING_RESPONSE = "Pong!"

    def __str__(self):
        return self.value

    @staticmethod
    def format_dice_roll_result(sides, result):
        """Formats the dice roll result message."""
        return Message.DICE_ROLL_RESULT.value.format(sides=sides, result=result)
