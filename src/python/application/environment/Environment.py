import os
from dataclasses import dataclass


@dataclass
class Environment:
    tokenBotDiscord: str
    openAIApiKey: str
    openAIAssistantId: str

    @staticmethod
    def load():
        tokenBotDiscord = os.getenv('TOKEN_BOT_DISCORD')
        openAIApiKey = os.getenv('OPENIA_API_KEY')
        openAIAssistantId = os.getenv('GPT_ASSISTANT_ID')

        return Environment(
            tokenBotDiscord=tokenBotDiscord,
            openAIApiKey=openAIApiKey,
            openAIAssistantId=openAIAssistantId
        )
