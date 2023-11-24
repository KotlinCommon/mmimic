from src.python.application.Either import Either
from src.python.domain.EndPoint import EndPoint


def createCharacter(client, userId, name, backstory):
    # Prepare the data for the PUT request
    characterData = {
        "userId": userId,
        "name": name,
        "backstory": backstory
    }
    response = client.put(EndPoint.character, characterData)

    # Handle the response
    if response.is_success():
        newCharacterData = response.value
        return Either.Success(newCharacterData)
    else:
        print(f"{response.value}")
        if response.value and 'error' in response.value:
            errorDetail = response.value.get('error')
            errorMessage = response.value.get('message', 'No additional message provided.')
            print(f"Error: {errorDetail}, Message: {errorMessage}")
            return Either.Failure(f"Error: {errorDetail}, Message: {errorMessage}")
        else:
            return Either.Failure(False)
