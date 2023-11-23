from src.python.domain.message.Message import Message
from src.python.domain.user.SignUp import signUp
from src.python.domain.user.User import User


async def registerUser(client, userState, message):
    userState.setUserState(message.author.id, "REGISTERING")
    user = User(None, "mimic@", message.author.name, message.author.id)
    result = signUp(client, user)
    userState.resetUserState(message.author.id)

    if result.isSuccess():
        return f"{Message.RegistrationComplete}"
    else:
        return f"{Message.AlreadyRegistered}"
