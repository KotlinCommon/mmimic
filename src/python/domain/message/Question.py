from enum import Enum

from src.python.domain.util.ValidEmail import ValidEmail


class Question(Enum):
    RegisterUser = [
        ("What's your name?", None),
        #("What's your email?", ValidEmail)
        ("What's your email?", None)
    ]

    def __str__(self):
        return ', '.join([q[0] for q in self.value])
