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
            dmChannel = await user.create_dm()
            await self.startRegistrationProcess(user, dmChannel)
        except Exception as e:
            await ctx.send(Message.Error.formatError(e))

    @commands.command(name='rollDice')
    async def rollDice(self, ctx, sides: int = 6):
        """Rolls a dice with a specified number of sides."""
        roll = rollDice(sides)
        if roll is None:
            await ctx.send(Message.DiceRollInvalidSides)
        else:
            await ctx.send(Message.formatDiceRollResult(sides, roll))

    async def startRegistrationProcess(self, user, dmChannel):
        fakeMessage = type('obj', (object,), {'author': user, 'channel': dmChannel})
        messageToReturn = await registerUserDirect(self, self.bot, self.client, fakeMessage, self.userState)
        if messageToReturn:
            await dmChannel.send(messageToReturn)
