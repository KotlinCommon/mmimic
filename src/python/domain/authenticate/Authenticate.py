from src.python.domain.message.ErrorMessage import ErrorMessage
from src.python.domain.EndPoint import EndPoint


def authenticate(client, credentials):
    """
    Authenticate the user and return the Bearer token.
    """
    response = client.post(EndPoint.SignInBot, credentials)
    if response.is_success():
        # Extracting the token from the Authorization header
        auth_header = response.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            return auth_header
        else:
            print(ErrorMessage.TokenNotFound)
            return None
    else:
        print(f"{ErrorMessage.AuthenticationFailed}{response.error}")
        return None
