from discord.ext import commands

from src.python.domain.message.Message import Message


class CharacterCommand(commands.Cog):
    def __init__(self, bot, client, userState):
        self.bot = bot
        self.client = client
        self.userState = userState

    @commands.group(
        name='character',
        invoke_without_command=True,
        brief="- See all character commands : !help character"
    )
    async def character(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Available subcommands: list")

    @character.command(name='list', brief="- List all characters")
    async def characters(self, ctx):
        await ctx.send(Message.InProduction)

    async def getCharacterGroup(self):
        return self.character
