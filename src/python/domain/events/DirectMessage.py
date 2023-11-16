import discord

from src.python.domain.message.Message import Message


class DirectMessage:
    def __init__(self, openai_client):
        self.openai_client = openai_client

    async def process(self, message):
        # Avoid responding to own message
        if message.author.bot:
            return

        response = await self.response(message.content)
        await message.channel.send(response)

    async def response(self, message):
        # Placeholder for response generation logic
        return f"{Message.DIRECT_MESSAGE_RECEIVED}{message}"

        # Example: return await self.openai_client.askGpt3(message_content)
