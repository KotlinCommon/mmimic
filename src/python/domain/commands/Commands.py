from src.python.domain.commands.GeneralCommands import GeneralCommands
from src.python.domain.commands.FunCommands import FunCommands


class Commands:
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState

    async def registerCommands(self):
        await self.bot.add_cog(GeneralCommands(self.bot, self.client, self.userState))
        await self.bot.add_cog(FunCommands(self.bot))

    # Example command using MessageType
