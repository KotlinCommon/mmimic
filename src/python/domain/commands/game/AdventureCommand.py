import discord
from discord.ext import commands

from src.python.domain.message.Message import Message
from src.python.domain.network.user.GetUser import getUser
from src.python.domain.network.user.User import User


class AdventureCommand(commands.Cog):
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState

    @commands.group(
        name='adventure',
        invoke_without_command=True,
        brief="- See all adventure commands : !help adventure"
    )
    async def adventure(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Available subcommands: list")

    @adventure.command(name='list', brief="- List all adventure")
    async def adventures(self, ctx):
        await ctx.send(Message.InProduction)

    @commands.command(name="startAdventure")
    async def startAdventure(self, ctx):
        channelId = ctx.channel.id
        userId = ctx.author.id

        # Check if user is registered
        verifyRegister = getUser(self.client, userId)
        if not verifyRegister:
            await ctx.send("You need to register before starting a story session. send {!register}")
            return

        if channelId in self.bot.activeAdventureSessions:
            await ctx.send(Message.AdventureAlreadyActive)
            return
        self.bot.activeAdventureSessions[channelId] = userId
        await ctx.send(f"{ctx.author.mention} {Message.AdventureStarted}")

    @commands.command(name="endAdventure")
    async def endAdventure(self, ctx):
        channelId = ctx.channel.id
        userId = ctx.author.id

        # Check if this user has an active session in this channel
        if self.bot.activeAdventureSessions.get(channelId) == userId:
            del self.bot.activeAdventureSessions[channelId]
            await ctx.send(Message.AdventureEnd)
        else:
            await ctx.send(Message.AdventureNotActive)

    async def getAdventureGroup(self):
        return self.adventure
