class AdventureSession:
    def __init__(self):
        self.sessions = {}

    def start_session(self, channelId, user):
        self.sessions[channelId] = user

    def end_session(self, channelId):
        if channelId in self.sessions:
            del self.sessions[channelId]

    def is_session_active(self, channelId):
        return self.sessions.get(channelId)

    def get_session_user(self, channelId):
        return self.sessions.get(channelId)
