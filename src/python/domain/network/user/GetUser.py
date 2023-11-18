from src.python.domain.network.EndPoint import EndPoint


def getUser(client, discordId):
    """
    Authenticate the user and return the Bearer token.
    """
    response = client.put(EndPoint.userWithDiscordId(discordId))

    if response.isSuccess():
        return "Test get user"
    else:
        if response.value and 'error' in response.value:
            error_detail = response.value.get('error')
            error_message = response.value.get('message', 'No additional message provided.')
            print(f"Error: {error_detail}, Message: {error_message}")
        else:
            print(f"Failed to register user. Error: {response.error}")

        return None
