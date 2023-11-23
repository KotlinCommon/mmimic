from src.python.domain.character.GetCharacters import getCharacters
from src.python.domain.message.Message import Message


class AdventureSession:
    def __init__(self):
        self.sessions = {}
        self.client = None
        self.bot = None

    async def startSession(self, ctx, channelId, user, bot, client):
        self.sessions[channelId] = user
        self.client = client
        self.bot = bot

        await self.showUserCharacters(ctx, user.id)

    async def showUserCharacters(self, ctx, userId):
        print(userId)
        userCharacters = getCharacters(self.client, userId)  # Updated to use bot directly
        if userCharacters:
            characterList = '\n'.join([f"{char.id}: {char.name}" for char in userCharacters])
            await ctx.send(f"Your characters:\n{characterList}")
        else:
            await ctx.send("You have no characters. Use the command to create a new one.")

    def endSession(self, channelId):
        if channelId in self.sessions:
            del self.sessions[channelId]

    def isSessionActive(self, channelId):
        return self.sessions.get(channelId)

    def getSessionUser(self, channelId):
        return self.sessions.get(channelId)
