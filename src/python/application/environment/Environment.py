import os
from dataclasses import dataclass


@dataclass
class Environment:
    tokenBotDiscord: str
    openAIApiKey: str
    serverId: int
    gptSystem: str

    @staticmethod
    def load():
        tokenBotDiscord = os.getenv('TOKEN_BOT_DISCORD')
        openAIApiKey = os.getenv('GPT_API_KEY')
        gptSystem = loadGptSystem()
        return Environment(
            tokenBotDiscord=tokenBotDiscord,
            openAIApiKey=openAIApiKey,
            serverId=1179050345645744199,
            gptSystem=gptSystem
        )


def loadGptSystem():
    projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
    gptSystemPath = os.path.join(projectRoot, '.docker', 'gptSystem.txt')

    with open(gptSystemPath, 'r') as file:
        return file.read()
