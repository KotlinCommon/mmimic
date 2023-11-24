from typing import List

from src.python.domain.EndPoint import EndPoint
from src.python.domain.adventure.character.Character import Character
from src.python.domain.adventure.character.equipped.Equipped import Equipped


def getCharacters(client, userId) -> List[Character]:
    response = client.get(EndPoint.charactersWithUserId(userId), None)

    if response.is_success():
        charactersData = response.value
        characters = []
        for charData in charactersData:
            # Check if 'equipped' key exists
            equippedData = charData.get('equipped')
            if equippedData:
                equipped = Equipped(
                    id=equippedData['id'],
                    characterId=equippedData['characterId'],
                    helmetId=equippedData.get('helmetId', 0),  # Provide default values if keys might be missing
                    gloveId=equippedData.get('gloveId', 0),
                    armourId=equippedData.get('armourId', 0),
                    bootId=equippedData.get('bootId', 0),
                    weaponId=equippedData.get('weaponId', 0),
                    ringId=equippedData.get('ringId', 0),
                    amuletId=equippedData.get('amuletId', 0),
                    createAt=equippedData.get('createAt', 0),
                    updateAt=equippedData.get('updateAt', 0)
                )
            else:
                equipped = None  # Or some default Equipped object

            character = Character(
                id=charData['id'],
                userId=charData['userId'],
                name=charData['name'],
                backstory=charData['backstory'],
                storiesIdentifier=charData['storiesIdentifier'],
                equipped=equipped,
                createAt=charData['createAt'],
                updateAt=charData['updateAt'],
            )
            characters.append(character)
        return characters
    else:
        # Handling error messages as before
        return None
