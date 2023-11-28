from src.python.domain.commands.AdventureCommands import AdventureCommands
from src.python.domain.commands.GeneralCommands import GeneralCommands
from src.python.domain.events.Events import Events


class Commands:
    def __init__(self, bot):
        self.bot = bot

    async def registerCommands(self):
        await self.bot.add_cog(Events(self.bot))
        await self.bot.add_cog(GeneralCommands(self.bot))
        await self.bot.add_cog(AdventureCommands(self.bot))
