from src.python.domain.EndPoint import EndPoint


def createCharacter(client, userId, name, backstory):
    response = client.get(EndPoint.userWithDiscordId(userId), None)

    """""
    if response.is_success():
        user_data = response.value
        return User(email=user_data['email'], name=user_data['name'], discordId=user_data['discordId'])
    else:
        # Handling error messages as before
        return None
    """