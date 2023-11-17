from dataclasses import dataclass, asdict


@dataclass
class User:
    email: str
    name: str
    discordId: str

    def serializable(self):
        return asdict(self)
