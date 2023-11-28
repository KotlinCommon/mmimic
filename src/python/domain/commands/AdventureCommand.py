from discord.ext import commands

from src.python.domain.adventure.AdventureSession import AdventureSession
from src.python.domain.message.Message import Message
from src.python.domain.network.GetUser import getUser


class AdventureCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name='adventure',
        invoke_without_command=True,
        brief="- See all adventure commands : !help adventure"
    )
    async def adventure(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Available subcommands: list")

    @commands.command(name="start")
    async def start(self, ctx):
        channelId = ctx.channel.id
        userId = ctx.author.id

        if self.activeSession.getSessionUser(channelId):
            await ctx.send(Message.AdventureAlreadyActive)
            return

        await ctx.send(f"{ctx.author.mention} {Message.AdventureStarted}")
        await self.activeSession.startSession(ctx, channelId, self.bot)

    @commands.command(name="end")
    async def end(self, ctx):
        channelId = ctx.channel.id
        if self.activeSession.getSessionUser(channelId):
            self.activeSession.endSession(channelId)
            await ctx.send(Message.AdventureEnd)
        else:
            await ctx.send(Message.AdventureNotActive)
