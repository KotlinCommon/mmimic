import discord
from discord.ext import commands
import asyncio

from src.python.application.environment.SetupIntents import setupIntents
from src.python.application.environment.BuildEnvironment import buildEnvironment
from src.python.application.environment.Environment import Environment
from src.python.domain.events.Events import Events
from src.python.domain.commands.Commands import Commands

from src.python.application.client.Client import Client


class MimicBot:
    def __init__(self, commandPrefix="!"):
        buildEnvironment()
        self.environment = Environment.load()

        self.client = Client(self.environment.urlBackend)

        self.bot = commands.Bot(command_prefix=commandPrefix, intents=setupIntents())
        self.events = Events(self.bot)
        self.commands = Commands(self.bot, self)

    async def setup(self):
        await self.commands.registerCommands()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.setup())  # Run the setup before starting the bot
        self.bot.run(self.environment.tokenBotDiscord)
