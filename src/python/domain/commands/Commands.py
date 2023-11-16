
from src.python.domain.commands.GeneralCommands import GeneralCommands
from src.python.domain.commands.FunCommands import FunCommands


class Commands:
    def __init__(self, bot, mimicBot):
        self.bot = bot
        self.mimicBot = mimicBot  # Store the reference to MimicBot

    async def registerCommands(self):
        await self.bot.add_cog(GeneralCommands(self.bot))
        await self.bot.add_cog(FunCommands(self.bot))

    # Example command using MessageType
