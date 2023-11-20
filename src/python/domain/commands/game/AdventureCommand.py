import discord
from discord.ext import commands

from src.python.domain.message.Message import Message


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

    @commands.command(name="startStory")
    async def startStory(self, ctx):
        channel_id = ctx.channel.id
        user_id = ctx.author.id
        if channel_id in self.bot.activeAdventureSessions:
            await ctx.send("A story session is already active in this channel.")
            return
        self.bot.activeAdventureSessions[channel_id] = user_id
        await ctx.send(f"{ctx.author.mention} has started a new story session.")

    @commands.command(name="endStory")
    async def endStory(self, ctx):
        channel_id = ctx.channel.id
        user_id = ctx.author.id

        # Check if this user has an active session in this channel
        if self.bot.activeAdventureSessions.get(channel_id) == user_id:
            del self.bot.activeAdventureSessions[channel_id]
            await ctx.send("Your story session has ended.")
        else:
            await ctx.send("You do not have an active story session in this channel.")

    async def getAdventureGroup(self):
        return self.adventure
