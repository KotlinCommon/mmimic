from src.python.domain.network.EndPoint import EndPoint
from src.python.domain.network.user.User import User


def getUser(client, discordId):
    response = client.get(EndPoint.userWithDiscordId(discordId), None)

    if response.is_success():
        user_data = response.value
        return User(email=user_data['email'], name=user_data['name'], discordId=user_data['discordId'])
    else:
        # Handling error messages as before
        return None
