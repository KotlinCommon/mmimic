import asyncio

from src.python.domain.events.InteractiveSession import InteractiveSession
from src.python.domain.message.Message import Message
from src.python.domain.message.Question import Question
from src.python.domain.network.user.RegisterUser import registerUser
from src.python.domain.network.user.User import User


async def registerUserDirect(self, bot, client, message, userState):
    userState.setUserState(message.author.id, "REGISTERING")
    session = InteractiveSession(bot, Question.RegisterUser)
    responses = await session.run(message)

    if responses is not None:
        user = User("", "", message.author.id)
        for index, response in enumerate(responses):
            if index == 0:
                user.name = response  # First response is name
            elif index == 1:
                user.email = response  # Second response is email

        registerUser(client, user)
        return Message.RegistrationComplete

    else:
        return Message.TookLongToRespond
