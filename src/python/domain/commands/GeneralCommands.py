from discord.ext import commands

from src.python.domain.message.Message import Message


class GeneralCommands(commands.Cog, name="General Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(Message.PingResponse)
