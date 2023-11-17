import asyncio

from src.python.domain.message.Message import Message


class InteractiveSession:
    def __init__(self, bot, question_validation_pairs):
        self.bot = bot
        self.question_validation_pairs = [(q[0], q[1]) for q in question_validation_pairs.value]
        self.responses = []

    async def run(self, message):
        for question, validation in self.question_validation_pairs:
            await message.channel.send(question)

            while True:
                def check(m):
                    return m.author == message.author and m.channel == message.channel

                try:
                    response = await self.bot.wait_for('message', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    await message.channel.send(Message.TookLongToRespond)
                    return None  # Session ended due to timeout

                if validation and not validation(response.content):
                    await message.channel.send(Message.formatInvalidInput(response.content))
                    continue  # Ask the same question again

                self.responses.append(response.content)
                break  # Break the loop and move to the next question

        return self.responses
