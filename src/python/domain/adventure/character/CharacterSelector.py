from src.python.domain.adventure.character.CreateNewCharacter import createNewCharacter
from src.python.domain.message.Message import Message
from src.python.domain.network.GetCharacters import getCharacters


async def selectCharacter(self, ctx, userId):
    userCharacters = getCharacters(self.client, userId)
    if userCharacters:
        characterList = '\n'.join([f"{index} - {char.name}" for index, char in enumerate(userCharacters, start=1)])
        await ctx.send(Message.formatCharacterList(characterList))

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        response = await self.bot.wait_for('message', check=check)  # Wait for user response
        if response.content.lower() == 'new':
            # Create new character logic
            await createNewCharacter(self, ctx, userId)
        elif response.content.isdigit() and 1 <= int(response.content) <= len(userCharacters):
            selectedCharacter = userCharacters[int(response.content) - 1]
            self.sessions[ctx.channel.id]["character"] = selectedCharacter

            await ctx.send(Message.formatCharacterSelectedInfo(selectedCharacter))

            # Ask for next action
            await ctx.send(Message.StartAdventurePrompt)
            response = await self.bot.wait_for('message', check=check)
            if response.content.lower() == 'change':
                await selectCharacter(self, ctx, userId)  # Show characters again for re-selection
            elif response.content.lower() == 'start':
                await ctx.send(Message.StartAdventureConfirmation)
                # Implement adventure start logic
        else:
            await ctx.send(Message.InvalidCharacterChoice)
            await selectCharacter(self, ctx, userId)  # Show characters again for re-selection
    else:
        await createNewCharacter(self, ctx, userId)
