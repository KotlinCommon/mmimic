from enum import Enum

from src.python.domain.util.ValidEmail import ValidEmail


class AdventureQuestion(Enum):
    StartAdventure = [
        ("What's your name?", None),
        ("What's your email?", ValidEmail)
    ]

    def __str__(self):
        return ', '.join([q[0] for q in self.value])
