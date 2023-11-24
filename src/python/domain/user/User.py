from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class User:
    email: str
    name: str
    discordId: str
    id: Optional[int] = None

    def serializable(self):
        return asdict(self)
