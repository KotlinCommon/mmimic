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

    async def getAdventureGroup(self):
        return self.adventure
