from discord.ext import commands

from src.python.application.client.GPTClient import GPTClient


class AdventureSession:
    def __init__(self, gptKey):
        self.gptKey = gptKey
        self.activeSessions = {}

    def isSessionActive(self, guildId, channelId):
        return (guildId, channelId) in self.activeSessions

    async def startSession(self, guildId, channelId, userId):
        if (guildId, channelId) in self.activeSessions:
            return False

        gptClient = GPTClient(self.gptKey)

        self.activeSessions[(guildId, channelId)] = {
            "userId": userId,
            "gptClient": gptClient
        }
        return True

    def endSession(self, guildId, channelId):
        if self.isSessionActive(guildId, channelId):
            del self.activeSessions[(guildId, channelId)]

    def getSessionStarter(self, guildId, channelId):
        session = self.activeSessions.get((guildId, channelId))
        if session:
            return session.get("userId")
        return None

    def getGPTClient(self, guildId, channelId):
        return self.activeSessions.get((guildId, channelId), {}).get("gptClient")
