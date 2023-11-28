from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.bot.user:
            return

        # Error handling for DMs or missing information
        if not message.guild or not message.channel:
            return

        # Check if there is an active adventure session
        if self.bot.adventure_sessions.isSessionActive(message.guild.id, message.channel.id):
            session_starter_id = self.bot.adventure_sessions.getSessionStarter(message.guild.id, message.channel.id)

            # If the message author is not the session starter, delete the message
            if message.author.id != session_starter_id:
                await message.delete()
