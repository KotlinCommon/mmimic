class AdventureSession:
    def __init__(self):
        self.sessions = {}

    def startSession(self, channelId, user):
        self.sessions[channelId] = user

    def endSession(self, channelId):
        if channelId in self.sessions:
            del self.sessions[channelId]

    def isSessionActive(self, channelId):
        return self.sessions.get(channelId)

    def getSessionUser(self, channelId):
        return self.sessions.get(channelId)
