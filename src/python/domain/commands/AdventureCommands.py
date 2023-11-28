from discord.ext import commands

from src.python.domain.adventure.AdventureSession import AdventureSession


class AdventureCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="start")
    async def start(self, ctx):
        if not ctx.guild or not ctx.channel:
            await ctx.send("This command cannot be used in direct messages.")
            return

        if self.bot.adventure_sessions.startSession(ctx.guild.id, ctx.channel.id, ctx.author.id):
            await ctx.send(f"Adventure session started for {ctx.author.mention} in this channel.")

    @commands.command(name="end")
    async def end(self, ctx):
        if not ctx.guild or not ctx.channel:
            await ctx.send("This command cannot be used in direct messages.")
            return

        if self.bot.adventure_sessions.getSessionStarter(ctx.guild.id, ctx.channel.id) == ctx.author.id:
            self.bot.adventure_sessions.end_session(ctx.guild.id, ctx.channel.id)
            await ctx.send(f"Adventure session ended for {ctx.author.mention} in this channel.")
