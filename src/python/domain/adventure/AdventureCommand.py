from discord.ext import commands

from src.python.domain.adventure.AdventureSession import AdventureSession
from src.python.domain.character.GetCharacters import getCharacters
from src.python.domain.message.Message import Message
from src.python.domain.user.GetUser import getUser


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

    @commands.command(name="start")
    async def start(self, ctx):
        channelId = ctx.channel.id
        userId = ctx.author.id

        user = getUser(self.client, userId)
        if user is None:
            await ctx.send(f"{Message.NeedRegister}")
            return

        if self.activeSession.getSessionUser(channelId):
            await ctx.send(Message.AdventureAlreadyActive)
            return

        await ctx.send(f"{ctx.author.mention} {Message.AdventureStarted}")
        await self.activeSession.startSession(ctx, channelId, user, self.bot, self.client)

    @commands.command(name="end")
    async def end(self, ctx):
        channelId = ctx.channel.id
        print(f"{self.activeSession}")

        if self.activeSession.getSessionUser(channelId):
            self.activeSession.endSession(channelId)
            await ctx.send(Message.AdventureEnd)
        else:
            await ctx.send(Message.AdventureNotActive)
