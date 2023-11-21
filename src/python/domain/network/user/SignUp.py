from src.python.application.Either import Either
from src.python.domain.network.EndPoint import EndPoint


def signUp(client, user):
    """
    Authenticate the user and return an Either object.
    """
    response = client.put(EndPoint.SignUp, user.serializable())

    if response.is_success():
        print(f"{response}")
        return Either.Success(True)
    else:
        print(f"{response.value}")
        if response.value and 'error' in response.value:
            error_detail = response.value.get('error')
            error_message = response.value.get('message', 'No additional message provided.')
            print(f"Error: {error_detail}, Message: {error_message}")
            return Either.Failure(f"Error: {error_detail}, Message: {error_message}")
        else:
            return Either.Failure(False)
