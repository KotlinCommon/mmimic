from dataclasses import dataclass, asdict


@dataclass
class Equipped:
    id: int
    characterId: int
    helmetId: int
    gloveId: int
    armourId: int
    bootId: int
    weaponId: int
    ringId: int
    amuletId: int

    def serializable(self):
        return asdict(self)
