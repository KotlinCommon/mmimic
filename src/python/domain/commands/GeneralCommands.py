from discord.ext import commands
from src.python.domain.message.Message import Message
from src.python.domain.util.RollDice import rollDice


class GeneralCommands(commands.Cog, name="General Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rollDice')
    async def roll_dice_command(self, ctx, sides: int = 6):
        """Rolls a dice with a specified number of sides."""
        roll = rollDice(sides)
        if roll is None:
            await ctx.send("The number of sides must be at least 1.")
        else:
            await ctx.send(f"You rolled a {sides}-sided dice and got: {roll}")