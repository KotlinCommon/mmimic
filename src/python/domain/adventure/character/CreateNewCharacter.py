from src.python.domain.adventure.character.Character import Character
from src.python.domain.message.Message import Message
from src.python.domain.network.CreateCharacter import createCharacter


async def createNewCharacter(self, ctx, userId):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send(Message.EnterCharacterName)
    name_response = await self.bot.wait_for('message', check=check)

    await ctx.send(Message.EnterCharacterBackstory)
    backstory_response = await self.bot.wait_for('message', check=check)

    # Confirm character creation
    confirmation_msg = Message.formatConfirmCharacterCreation(name_response.content, backstory_response.content)
    await ctx.send(confirmation_msg)

    confirm_response = await self.bot.wait_for('message', check=check)

    if confirm_response.content.lower() == 'save':
        creation_result = createCharacter(self.client, userId, name_response.content, backstory_response.content)
        if creation_result.isSuccess():
            new_character_data = creation_result.value
            self.sessions[ctx.channel.id]["character"] = Character(**new_character_data)
            await ctx.send(Message.CharacterCreatedSuccess)
        else:
            await ctx.send(Message.CharacterCreationFailed)
            await self.createNewCharacter(ctx, userId)
    elif confirm_response.content.lower() == 'redo':
        await self.createNewCharacter(ctx, userId)  # Restart the character creation process
    else:
        await ctx.send(Message.InvalidCreationResponse)
        await self.createNewCharacter(ctx, userId)
