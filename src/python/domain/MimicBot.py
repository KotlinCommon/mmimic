from discord.ext import commands
import asyncio

from src.python.application.environment.SetupIntents import setupIntents
from src.python.application.environment.BuildEnvironment import buildEnvironment
from src.python.application.environment.Environment import Environment
from src.python.domain.events.Events import Events
from src.python.domain.commands.Commands import Commands

from src.python.application.client.Client import Client
from src.python.domain.events.UserState import UserState
from src.python.domain.network.authenticate.Authenticate import authenticate
from src.python.domain.network.authenticate.Credential import Credential


class MimicBot:
    def __init__(self, commandPrefix="!"):
        buildEnvironment()
        self.environment = Environment.load()

        self.client = Client(self.environment.urlBackend)
        self.client.bearerToken = self.authenticateBot()

        self.bot = commands.Bot(command_prefix=commandPrefix, intents=setupIntents())
        self.userState = UserState()
        self.events = Events(self.environment, self.bot, self.client, self.userState)
        self.commands = Commands(self.bot, self.client, self.userState)

    def authenticateBot(self):
        credentials = Credential(
            identifier=self.environment.identifier,
            password=self.environment.password
        ).serializable()
        return authenticate(self.client, credentials)

    async def setup(self):
        await self.commands.registerCommands()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.setup())  # Run the setup before starting the bot
        self.bot.run(self.environment.tokenBotDiscord)
