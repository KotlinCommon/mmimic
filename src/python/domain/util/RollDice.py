import random


def rollDice(sides):
    """Rolls a dice and returns the result."""
    if sides < 1:
        return None
    return random.randint(1, sides)
