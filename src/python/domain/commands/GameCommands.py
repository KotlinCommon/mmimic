from discord.ext import commands

from src.python.domain.adventure.AdventureCommand import AdventureCommand


class GameCommands(commands.Cog, name="Game Commands"):
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState

    @commands.Cog.listener()
    async def on_ready(self):
        await self.loadAdventureCommands()

    async def loadAdventureCommands(self):
        adventureCmds = AdventureCommand(self.bot, self.client, self.userState)
        await self.bot.add_cog(adventureCmds)
