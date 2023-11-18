from discord.ext import commands

from src.python.domain.events.directMessage.RegisterUserDirect import registerUserDirect
from src.python.domain.message.Message import Message
from src.python.domain.util.RollDice import rollDice


class GeneralCommands(commands.Cog, name="General Commands"):
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState

    @commands.command(name='register')
    async def register(self, ctx):
        user = ctx.message.author

        try:
            dm_channel = await user.create_dm()
            await self.start_registration_process(user, dm_channel)

        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='rollDice')
    async def rollDice(self, ctx, sides: int = 6):
        """Rolls a dice with a specified number of sides."""
        roll = rollDice(sides)
        if roll is None:
            await ctx.send(Message.DiceRollInvalidSides)
        else:
            await ctx.send(Message.formatDiceRollResult(sides, roll))

    async def start_registration_process(self, user, dm_channel):
        fake_message = type('obj', (object,), {'author': user, 'channel': dm_channel})
        message_to_return = await registerUserDirect(self, self.bot, self.client, fake_message, self.userState)
        if message_to_return:
            await dm_channel.send(message_to_return)
