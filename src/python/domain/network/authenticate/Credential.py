from dataclasses import dataclass, asdict


@dataclass
class Credential:
    identifier: str
    password: str

    def serializable(self):
        return asdict(self)
