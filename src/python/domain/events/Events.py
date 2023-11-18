import discord

from src.python.domain.events.directMessage.DirectMessage import DirectMessage


class Events:
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState
        self.directMessage = DirectMessage(self.bot, self.client, self.userState)
        self.registerEvents()

    def registerEvents(self):
        @self.bot.event
        async def on_ready():
            print(f"Logged in as {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            author = message.author
            channel = message.channel
            userId = author.id
            print(userId, " - ", author, "in channel (", channel, ") send Message:", message.content)

            # Check if the message is a DM
            if isinstance(message.channel, discord.DMChannel):
                await self.directMessage.process(message)
            else:
                await self.bot.process_commands(message)

        # You can add more event handlers here
