from src.python.domain.events.guild.CreateRoom import createRoom
from src.python.domain.message.Message import Message


class Events:
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState
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
            session_user_id = self.bot.activeAdventureSessions.get(message.channel.id)
            if session_user_id and message.author.id != session_user_id:
                return

            if message.content.startswith(self.bot.command_prefix):
                author = message.author
                channel = message.channel
                userId = author.id
                # Check if the message is not in the bot-created room
                if channel.name != self.bot.environment.roomName:
                    await channel.send(Message.PleaseUseRoom.formatPleaseUseRoomInput(self.bot.environment.roomName))
                print(userId, " - ", author, "in channel (", channel, ") send Message:", message.content)
                await self.bot.process_commands(message)

            # Check if the message is a DM
            # if isinstance(message.channel, discord.DMChannel):
            # await self.directMessage.process(message)
            # else:

        @self.bot.event
        async def on_guild_join(guild):
            await createRoom(guild, self.bot.environment.roomName)
