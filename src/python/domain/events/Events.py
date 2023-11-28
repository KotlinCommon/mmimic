from src.python.domain.guild.CreateRoom import createRoom
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
            if message.author == self.bot.user:  # Ignore messages sent by the bot itself
                return

            if message.content.startswith(self.bot.command_prefix):
                author = message.author
                channel = message.channel
                userId = author.id
                if channel.name != self.bot.environment.roomName:
                    await channel.send(Message.PleaseUseRoom.formatPleaseUseRoomInput(self.bot.environment.roomName))
                print(userId, " - ", author, "in channel (", channel, ") send Message:", message.content)
                await self.bot.process_commands(message)

        @self.bot.event
        async def on_guild_join(guild):
            await createRoom(guild, self.bot.environment.roomName)
