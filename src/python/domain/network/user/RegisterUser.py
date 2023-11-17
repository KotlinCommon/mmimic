from src.python.domain.message.ErrorMessage import ErrorMessage
from src.python.domain.network.EndPoint import EndPoint


def registerUser(client, user):
    """
    Authenticate the user and return the Bearer token.
    """
    response = client.put(EndPoint.SignUp, user.serializable())

    if response.is_success():
        return "Registration successful."
    else:
        if response.value and 'error' in response.value:
            error_detail = response.value.get('error')
            error_message = response.value.get('message', 'No additional message provided.')
            print(f"Error: {error_detail}, Message: {error_message}")
        else:
            print(f"Failed to register user. Error: {response.error}")

        return None
