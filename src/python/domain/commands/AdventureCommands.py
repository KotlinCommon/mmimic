import asyncio

from discord.ext import commands

from src.python.domain.adventure.AdventureSession import AdventureSession
from src.python.domain.message.Message import Message


class AdventureCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="start")
    async def start(self, ctx):
        if not ctx.guild or not ctx.channel:
            await ctx.send(Message.AdventureCommandCannot)
            return

        sessionStarted = await self.bot.adventureSessions.startSession(ctx.guild.id, ctx.channel.id, ctx.author.id)
        if sessionStarted:
            gptClient = self.bot.adventureSessions.getGPTClient(ctx.guild.id, ctx.channel.id)
            if gptClient:
                await ctx.send(Message.formatAdventureStarted(ctx.author.mention))
        else:
            await ctx.send(Message.AdventureSessionAlready)

    @commands.command(name="end")
    async def end(self, ctx):
        if not ctx.guild or not ctx.channel:
            await ctx.send(Message.AdventureCannotUsed)
            return

        if self.bot.adventureSessions.getSessionStarter(ctx.guild.id, ctx.channel.id) == ctx.author.id:
            self.bot.adventureSessions.endSession(ctx.guild.id, ctx.channel.id)
            await ctx.send(Message.formatAdventureEnded(ctx.author.mention))
        else:
            await ctx.send(Message.AdventureNotStarted)
