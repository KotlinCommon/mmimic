from discord.ext import commands
from src.python.domain.message.Message import Message
from src.python.domain.util.RollDice import rollDice


class GeneralCommands(commands.Cog, name="General Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rollDice')
    async def rollDice(self, ctx, sides: int = 6):
        """Rolls a dice with a specified number of sides."""
        roll = rollDice(sides)
        if roll is None:
            await ctx.send(Message.DiceRollInvalidSides)
        else:
            await ctx.send(Message.formatDiceRollResult(sides, roll))
