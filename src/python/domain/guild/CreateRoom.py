import discord


async def createRoom(guild, roomName):
    print(f"Joined new guild: {guild.name}")  # Debugging print

    existingRoom = discord.utils.get(guild.text_channels, name=roomName)
    if not existingRoom:
        print("Creating new room...")  # Debugging print
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        try:
            await guild.create_text_channel(roomName, overwrites=overwrites)
            print(f"Room '{roomName}' created successfully")  # Debugging print
        except Exception as e:
            print(f"Error in creating room: {e}")  # Debugging print
