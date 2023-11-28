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
        serverId = os.getenv('SERVER_ID')
        return Environment(
            tokenBotDiscord=tokenBotDiscord,
            openAIApiKey=openAIApiKey,
            roomName=roomName,
            serverId=serverId
        )
