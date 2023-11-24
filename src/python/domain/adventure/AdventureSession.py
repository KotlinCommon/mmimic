from src.python.domain.adventure.character.CharacterSelector import selectCharacter


class AdventureSession:
    def __init__(self):
        self.sessions = {}
        self.client = None
        self.bot = None
        self.isEnding = False

    async def startSession(self, ctx, channelId, user, bot, client):
        self.sessions[channelId] = {"user": user}
        self.client = client
        self.bot = bot
        await selectCharacter(self, ctx, user.id)

    def endSession(self, channelId):
        if channelId in self.sessions:
            del self.sessions[channelId]
            self.isEnding = True

    def isSessionActive(self, channelId):
        return self.sessions.get(channelId)

    def getSessionUser(self, channelId):
        return self.sessions.get(channelId)
