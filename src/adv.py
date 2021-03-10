from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# userInput = 0
# while userInput != ("x" or "exit" or "Exit" or "X" or "Q" or "q"):


#     # Print the intro text
#     userPrompt = f'>>>'
#     fancyline = "»»————-------　★　-------————-««"
#     boringline = "———————————————————————————————"
#     dialogIntro = f'\n  Welcome to the game!\n  Please make a selection:\n'
#     dialogOptions = f'\n  Options go here\n'
#     dialogExit = f'{boringline}\n  Press "Q" to quit'


#     print(fancyline)
#     print(dialogIntro)
#     print(fancyline)
#     print(dialogOptions)
#     print(dialogExit)

#     # request input from the user
#     # needs to go after things that are printed otherwise it sits and waits for input
#     userInput = input(userPrompt)


# if _name_ == '_main_':
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/


# store user choice
choice = 0
choice_range = ["a","b","c","d"]

# print text outside game loop to make sure it's working
print(f"Game has loaded\n")

# game loop:
while choice != ("q" or "Q"):

    # print out the menu
    print(f"This is the game!")
    print(f"Choose an option from: {choice_range}\n")
    print(f"Press Q to quit\n")

    # request user input
    choice = str(input(f">>>")).lower()

    # define quit condition
    if choice == ("q"):
        # print the quit message
        print(f"Thanks for playing!")
        break

    #this choice does something
    elif choice == ("5"):
        print(f"You find the hidden treasure room!")

    # define valid input to continue without error message
    elif choice in choice_range:
        # print the users choice (outcome)
        print(f"You chose {choice}\n")

    else:
        # print an error message
        print(f"Huh? Try a different command or press Q to quit.")
