from dataclasses import dataclass, asdict


@dataclass
class User:
    id: int
    email: str
    name: str
    discordId: str

    def serializable(self):
        return asdict(self)
