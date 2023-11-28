from src.python.domain.message.Message import Message


class Events:
    def __init__(self, bot):
        self.bot = bot
        self.registerEvents()

    def registerEvents(self):
        @self.bot.event
        async def on_ready():
            print(f"Logged in as {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            await self.processMessage(message)

            author = message.author
            channel = message.channel
            userId = author.id

            print(userId, " - ", author, "in channel (", channel, ") send Message:", message.content)

    async def processMessage(self, message):
        if message.author == self.bot.user:  # Ignore messages sent by the bot itself
            return

        if message.guild.id == self.bot.environment.serverId:
            await self.bot.process_commands(message)
            return
        else:
            await message.channel.send(Message.AllowedServer)
            return
