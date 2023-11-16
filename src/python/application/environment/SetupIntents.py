import discord


def setupIntents():
    """
    Set up and return the required intents for the bot.
    """
    intents = discord.Intents.default()
    intents.messages = True
    intents.guilds = True
    intents.message_content = True
    return intents
