import os
from dataclasses import dataclass


@dataclass
class Environment:
    tokenBotDiscord: str
    openAIApiKey: str
    roomName: str
    serverId: int

    @staticmethod
    def load():
        tokenBotDiscord = os.getenv('TOKEN_BOT_DISCORD')
        openAIApiKey = os.getenv('OPENIA_API_KEY')
        roomName = "storyteller"
        serverId = 1179050345645744199
        return Environment(
            tokenBotDiscord=tokenBotDiscord,
            openAIApiKey=openAIApiKey,
            roomName=roomName,
            serverId=serverId
        )
