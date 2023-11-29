import asyncio

from discord.ext import commands

from src.python.domain.message.Message import Message


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
        if self.bot.adventureSessions.isSessionActive(message.guild.id, message.channel.id):
            sessionStarterId = self.bot.adventureSessions.getSessionStarter(message.guild.id, message.channel.id)
            if message.author.id != sessionStarterId:
                await message.delete()
                # notification = f"{message.author.mention}, you are not part of the current adventure session."
                # await message.channel.send(notification)
                return  # Skip processing this message further

            gptClient = self.bot.adventureSessions.getGPTClient(message.guild.id, message.channel.id)
            if gptClient:
                loadingMessage = await message.channel.send(Message.AdventureProcessing)
                response = await gptClient.getResponse(message.content)
                await loadingMessage.edit(content=response)
