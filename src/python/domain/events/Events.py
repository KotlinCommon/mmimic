from src.python.domain.adventure.AdventureSession import AdventureSession
from src.python.domain.events.guild.CreateRoom import createRoom
from src.python.domain.message.Message import Message


class Events:
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState
        self.activeSession = AdventureSession()
        # self.directMessage = DirectMessage(self.bot, self.client, self.userState)
        self.registerEvents()

    def registerEvents(self):
        @self.bot.event
        async def on_ready():
            print(f"Logged in as {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:  # Ignore messages sent by the bot itself
                return

            sessionUser = self.activeSession.getSessionUser(message.channel.id)
            if sessionUser and message.author.id != sessionUser.discordId:
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
