from discord.ext import commands

from src.python.domain.message.Message import Message
from src.python.domain.commands.game.CharacterCommand import CharacterCommand
from src.python.domain.commands.game.AdventureCommand import AdventureCommand


class GameCommands(commands.Cog, name="Game Commands"):
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState

    @commands.Cog.listener()
    async def on_ready(self):
        await self.loadCharacterCommands()
        await self.loadAdventureCommands()

    async def loadCharacterCommands(self):
        characterCmds = CharacterCommand(self.bot, self.client, self.userState)
        await self.bot.add_cog(characterCmds)

    async def loadAdventureCommands(self):
        adventureCmds = AdventureCommand(self.bot, self.client, self.userState)
        await self.bot.add_cog(adventureCmds)
