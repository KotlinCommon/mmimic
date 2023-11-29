import asyncio

from discord.ext import commands

from src.python.application.client.GPTClient import GPTClient


class AdventureSession:
    def __init__(self, bot, gptKey):
        self.bot = bot
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
        # Setup timeout task
        self.activeSessions[(guildId, channelId)]["timeoutTask"] = asyncio.create_task(
            self.end_session_after_timeout(guildId, channelId))

        return True

    def updateConversationHistory(self, guildId, channelId, message):
        if self.isSessionActive(guildId, channelId):
            self.activeSessions[(guildId, channelId)]["conversationHistory"].append(message)
            # Reset the timeout task
            self.activeSessions[(guildId, channelId)]["timeoutTask"].cancel()
            self.activeSessions[(guildId, channelId)]["timeoutTask"] = asyncio.create_task(
                self.end_session_after_timeout(guildId, channelId))

    def getConversationHistory(self, guildId, channelId):
        if self.isSessionActive(guildId, channelId):
            return self.activeSessions[(guildId, channelId)].get("conversationHistory", [])
        return []

    async def end_session_after_timeout(self, guildId, channelId, timeout=600):  # 600 seconds = 10 minutes
        await asyncio.sleep(timeout)
        if self.isSessionActive(guildId, channelId):
            # Send a timeout message to the channel
            channel = self.bot.get_channel(channelId)
            if channel:
                await channel.send("The adventure session has timed out due to inactivity.")
            self.endSession(guildId, channelId)

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
