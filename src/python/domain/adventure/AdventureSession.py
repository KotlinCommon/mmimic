from discord.ext import commands


class AdventureSession:
    def __init__(self):
        self.activeSessions = {}

    def isSessionActive(self, guildId, channelId):
        return (guildId, channelId) in self.activeSessions

    def startSession(self, guildId, channelId, userId):
        if self.isSessionActive(guildId, channelId):
            return False
        self.activeSessions[(guildId, channelId)] = userId
        return True

    def endSession(self, guildId, channelId):
        if self.isSessionActive(guildId, channelId):
            del self.activeSessions[(guildId, channelId)]

    def getSessionStarter(self, guildId, channelId):
        return self.activeSessions.get((guildId, channelId))
