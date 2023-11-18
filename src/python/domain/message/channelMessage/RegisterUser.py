from src.python.application.Either import Either
from src.python.domain.message.Message import Message
from src.python.domain.network.user.SignUpUser import signUpUser
from src.python.domain.network.user.User import User


async def registerUser(self, bot, client, userState, message):
    userState.setUserState(message.author.id, "REGISTERING")
    user = User("mimic@", message.author.name, message.author.id)
    result = signUpUser(client, user)
    userState.resetUserState(message.author.id)

    if result.isSuccess():
        return f"{Message.RegistrationComplete}"
    else:
        return f"{Message.AlreadyRegistered}"