from discord.ext import commands

from src.python.application.client.GPTClient import GPTClient


class AdventureSession:
    def __init__(self, gptKey):
        self.gptKey = gptKey
        self.activeSessions = {}

    def isSessionActive(self, guildId, channelId):
        return (guildId, channelId) in self.activeSessions

    async def startSession(self, guildId, channelId, userId):
        # Check if a session is already active in the given channel
        if (guildId, channelId) in self.activeSessions:
            return False

        gptClient = GPTClient(self.gptKey)

        # Initialize a new session with the necessary information
        self.activeSessions[(guildId, channelId)] = {
            "userId": userId,
            "gptClient": gptClient,
            "conversationHistory": []  # Initialize an empty conversation history
        }
        return True

    def updateConversationHistory(self, guildId, channelId, message):
        if self.isSessionActive(guildId, channelId):
            self.activeSessions[(guildId, channelId)]["conversationHistory"].append(message)

    def getConversationHistory(self, guildId, channelId):
        if self.isSessionActive(guildId, channelId):
            return self.activeSessions[(guildId, channelId)].get("conversationHistory", [])
        return []

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
