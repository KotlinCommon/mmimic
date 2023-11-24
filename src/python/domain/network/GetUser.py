from src.python.domain.EndPoint import EndPoint
from src.python.domain.user.User import User


def getUser(client, discordId):
    response = client.get(EndPoint.userWithDiscordId(discordId), None)

    if response.is_success():
        userData = response.value
        return User(id=userData['id'], email=userData['email'], name=userData['name'], discordId=userData['discordId'])
    else:
        # Handling error messages as before
        return None
