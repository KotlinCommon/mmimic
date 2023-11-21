import discord
from discord.ext import commands

from src.python.domain.adventure.AdventureSession import AdventureSession
from src.python.domain.message.Message import Message
from src.python.domain.network.user.GetUser import getUser
from src.python.domain.network.user.User import User


class AdventureCommand(commands.Cog):
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState
        self.activeSession = AdventureSession()

    @commands.group(
        name='adventure',
        invoke_without_command=True,
        brief="- See all adventure commands : !help adventure"
    )
    async def adventure(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Available subcommands: list")

    @commands.command(name="startAdventure")
    async def startAdventure(self, ctx):
        channelId = ctx.channel.id
        userId = ctx.author.id

        user = getUser(self.client, userId)
        if user is None:
            await ctx.send(f"{Message.NeedRegister}")
            return

        if self.activeSession.get_session_user(channelId):
            await ctx.send(Message.AdventureAlreadyActive)
            return

        self.activeSession.start_session(channelId, user)
        print(f"{self.activeSession.get_session_user(channelId)}")
        await ctx.send(f"{ctx.author.mention} {Message.AdventureStarted}")

    @commands.command(name="endAdventure")
    async def endAdventure(self, ctx):
        channelId = ctx.channel.id
        print(f"{self.activeSession}")

        if self.activeSession.get_session_user(channelId):
            self.activeSession.end_session(channelId)
            await ctx.send(Message.AdventureEnd)
        else:
            await ctx.send(Message.AdventureNotActive)
