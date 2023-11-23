from dataclasses import dataclass, asdict

from src.python.domain.character.equipped.Equipped import Equipped


@dataclass
class Character:
    id: int
    userId: int
    name: str
    backstory: str
    storiesIdentifier: str
    equipped: Equipped

    def serializable(self):
        return asdict(self)
