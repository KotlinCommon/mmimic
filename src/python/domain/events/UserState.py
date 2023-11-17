class UserState:
    def __init__(self):
        self.userStates = {}

    def setUserState(self, userId, state):
        self.userStates[userId] = state

    def getUserState(self, userId):
        return self.userStates.get(userId)

    def resetUserState(self, userId):
        self.userStates.pop(userId, None)
