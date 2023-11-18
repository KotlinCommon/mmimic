from src.python.domain.message.Message import Message
from src.python.domain.message.directMessage.RegisterUserDirect import registerUserDirect


class DirectMessage:
    def __init__(self, bot, client, userState):
        self.client = client
        self.bot = bot
        self.userState = userState

    async def process(self, message):
        if message.author.bot:
            return
        if self.userState.getUserState(message.author.id) == "REGISTERING":
            return

        response = await self.verifyMessage(message)
        if response:
            await message.channel.send(response)
        else:
            await message.channel.send(f"{Message.CanIHelpYou} \n {Message.ForRegister}")

    async def verifyMessage(self, message):
        match message.content:
            case "register":
                messageToReturn = await registerUserDirect(self, self.bot, self.client, message, self.userState)
                self.userState.resetUserState(message.author.id)  # Reset user state after registration
                return messageToReturn
