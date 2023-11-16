from discord.ext import commands
import random

from src.python.domain.message.Message import Message


class FunCommands(commands.Cog, name="Fun Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(Message.PING_RESPONSE)


