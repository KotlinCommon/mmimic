from src.python.domain.network.EndPoint import EndPoint
from src.python.domain.network.user.User import User


def getUser(client, discordId):
    response = client.get(EndPoint.userWithDiscordId(discordId), None)

    if response.is_success():
        # Extract user data from the response
        user_data = response.value
        # Create and return a User object
        # Assuming user_data contains keys 'email', 'name', and 'discordId'
        return User(email=user_data['email'], name=user_data['name'], discordId=user_data['discordId'])
    else:
        if response.value and 'error' in response.value:
            error_detail = response.value.get('error')
            error_message = response.value.get('message', 'No additional message provided.')
            print(f"Error: {error_detail}, Message: {error_message}")
        else:
            print(f"Failed to retrieve user. Error: {response.error}")

        return False
