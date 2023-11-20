import os
from dataclasses import dataclass


@dataclass
class Environment:
    tokenBotDiscord: str
    openAIApiKey: str
    openAIAssistantId: str
    urlBackend: str
    identifier: str
    password: str
    roomName: str

    @staticmethod
    def load():
        tokenBotDiscord = os.getenv('TOKEN_BOT_DISCORD')
        openAIApiKey = os.getenv('OPENIA_API_KEY')
        openAIAssistantId = os.getenv('GPT_ASSISTANT_ID')
        urlBackend = os.getenv('URL_BACKEND')
        identifier = os.getenv('IDENTIFIER')
        password = os.getenv('PASSWORD')
        roomName = "storyteller"
        return Environment(
            tokenBotDiscord=tokenBotDiscord,
            openAIApiKey=openAIApiKey,
            openAIAssistantId=openAIAssistantId,
            urlBackend=urlBackend,
            identifier=identifier,
            password=password,
            roomName=roomName
        )
