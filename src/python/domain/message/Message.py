from enum import Enum


class Message(Enum):
    Error = "An error occurred:"
    InProduction = "In production"

    # Messages related to Events
    DirectMsgReceived = "Received your message:"
    PleaseUseRoom = "Please use the '{input}' room for your messages."
    AdventureAlreadyActive = "A Adventure session is already active in this channel."
    AdventureStarted = " has started a new story session."
    AdventureEnd = "Your story session has ended."
    AdventureNotActive = "You do not have an active story session in this channel."
    NeedRegister = "You need to register before starting a story session. send [ !register ]"

    # Messages related to GeneralCommands
    DiceRollInvalidSides = "The number of sides must be at least 1."
    DiceRollResult = "You rolled a {sides}-sided dice and got: {result}"

    # Messages related to FunCommands
    PingResponse = "Pong!"

    # Messages related to signUp User
    RegistrationComplete = "Registration complete. Thank you!"
    AlreadyRegistered = "You are already registered"

    # Messages related to Character Selection
    CharacterList = "Your characters:\n{characterList}\n\n **Type the number of the character you want to choose, or type 'new' to create a new character.**"
    InvalidCharacterChoice = "Invalid choice. Please choose a valid character number or type 'new'."
    StartAdventurePrompt = "Type 'start' to begin your adventure with this character, or 'change' to choose another character."
    CharacterSelectedInfo = "Character Picked: {selectedCharacter}\n..."
    StartAdventureConfirmation = "Starting your adventure..."

    # Messages related to Character Creation
    EnterCharacterName = "Enter the name of your new character:"
    EnterCharacterBackstory = "Enter the backstory for your character:"
    ConfirmCharacterCreation = "Character Name: {name}\nBackstory: {backstory}\nType 'save' to confirm or 'redo' to start over."
    CharacterCreatedSuccess = "Character created successfully! \n Starting your adventure..."
    CharacterCreationFailed = "Failed to create character. Please try again."
    InvalidCreationResponse = "Invalid response. Character creation restart."

    # Messages related to Direct
    CanIHelpYou = "how can I help you ?"
    ForRegister = "for register send : register"
    TookLongToRespond = "You took too long to respond."
    InvalidInput = "Invalid input: {input}. Please try again."

    def __str__(self):
        return self.value

    @staticmethod
    def formatError(inputContent):
        """Formats the invalid input message."""
        return Message.Error.value.format(input=inputContent)

    @staticmethod
    def formatDiceRollResult(sides, result):
        """Formats the dice roll result message."""
        return Message.DiceRollResult.value.format(sides=sides, result=result)

    @staticmethod
    def formatInvalidInput(inputContent):
        """Formats the invalid input message."""
        return Message.InvalidInput.value.format(input=inputContent)

    @staticmethod
    def formatPleaseUseRoomInput(inputContent):
        """Formats the invalid input message."""
        return Message.PleaseUseRoom.value.format(input=inputContent)

    @staticmethod
    def formatCharacterList(characterList):
        """Formats the character list message."""
        return Message.CharacterList.value.format(characterList=characterList)

    @staticmethod
    def formatCharacterSelectedInfo(selectedCharacter):
        """Formats the character selected info message."""
        return Message.CharacterSelectedInfo.value.format(selectedCharacter=selectedCharacter)

    @staticmethod
    def formatConfirmCharacterCreation(name, backstory):
        """Formats the confirm character creation message."""
        return Message.ConfirmCharacterCreation.value.format(name=name, backstory=backstory)
