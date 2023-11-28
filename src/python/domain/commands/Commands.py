from src.python.domain.commands.GeneralCommands import GeneralCommands


class Commands:
    def __init__(self, bot):
        self.bot = bot

    async def registerCommands(self):
        await self.bot.add_cog(GeneralCommands(self.bot))
