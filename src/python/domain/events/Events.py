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
                await self.restrictChannelPermissions(message.channel)
                loadingMessage = await message.channel.send(Message.AdventureProcessing)
                # Update conversation history with the user's message
                self.bot.adventureSessions.updateConversationHistory(
                    message.guild.id, message.channel.id, {"role": "user", "content": message.content}
                )

                # Access the conversation history directly from the session
                session_data = self.bot.adventureSessions.activeSessions.get((message.guild.id, message.channel.id), {})
                conversationHistory = session_data.get("conversationHistory", [])

                # Get GPT response
                response = await gptClient.getResponse(conversationHistory, message.content)

                # Update conversation history with the bot's response
                self.bot.adventureSessions.updateConversationHistory(
                    message.guild.id, message.channel.id, {"role": "system", "content": response}
                )

                await loadingMessage.edit(content=response)
                await self.restoreChannelPermissions(message.channel)

    async def restrictChannelPermissions(self, channel):
        try:
            await channel.set_permissions(channel.guild.default_role, send_messages=False)
        except Exception as e:
            print(f"Failed to restrict channel permissions: {e}")

    async def restoreChannelPermissions(self, channel):
        try:
            await channel.set_permissions(channel.guild.default_role, send_messages=True)
        except Exception as e:
            print(f"Failed to restore channel permissions: {e}")
