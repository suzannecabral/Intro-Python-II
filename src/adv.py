from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room(
        "Outside Cave Entrance",
        """North of you, the cave mouth beckons"""
    ),

    'foyer':    Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east."""
    ),

    'overlook': Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""
    ),

    'narrow':   Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air."""
    ),

    'treasure': Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""
    ),
}

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

room['outside'].exits['n_to'].append(room['foyer'])
room['foyer'].exits['s_to'].append(room['outside'])
room['foyer'].exits['n_to'].append(room['overlook'])
room['foyer'].exits['e_to'].append(room['narrow'])
room['overlook'].exits['s_to'].append(room['foyer'])
room['narrow'].exits['w_to'].append(room['foyer'])
room['narrow'].exits['n_to'].append(room['treasure'])
room['treasure'].exits['s_to'].append(room['narrow'])

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

# store user choice
choice = 0
valid_choices = ["n","e","s","w","q"]

this_room = room['outside']
this_room_exits = this_room.exits

# new list from non-blank exits
# this_room_exits = [exit for exit in this_room.exits]

# print text outside game loop to make sure it's working
print(f"Game has loaded\n")
print(f"This room: {this_room}\n")
print(f"Exits: {this_room_exits}\n")

# game loop:
while choice != ("q" or "Q"):

    # print out the menu
    # print(f"Choose an option from: {valid_choices}\n")
    print(f"Press Q to quit\n")

    # request user input
    choice = str(input(f">>>")).lower()

    # define quit condition
    if choice == ("q"):
        # print the quit message
        print(f"Thanks for playing!")
        break

    if choice == ("n"):
        if this_room_exits['n_to']:
            print(f"You travel north\n")
            
        else:
            print(f"You can't go north from here\n")

    if choice == ("e"):
        if this_room_exits['e_to']:
            print(f"You travel east\n")
        else:
            print(f"You can't go east from here\n")

    if choice == ("s"):
        if this_room_exits['s_to']:
            print(f"You travel south\n")
            print(f"{this_room_exits['s_to']}")
        else:
            print(f"You can't go south from here\n")

    if choice == ("w"):
        if this_room_exits['w_to']:
            print(f"You travel west\n")
        else:
            print(f"You can't go west from here\n")

    # #this choice does something
    # elif choice == ("5"):
    #     print(f"You find the hidden treasure room!\n")
    #     print(f"{room['treasure']}\n")

    # define valid input to continue without error message
    elif choice in valid_choices:
        # print the users choice (outcome)
        continue

    else:
        # print an error message
        print(f"Huh? Try a different command or press Q to quit.")

# TODO bookmark: next steps
# - set current room when you type movement command
# - what is going on with current_exits display
# ---- it looks like it's appending onto a list of rooms
# - ? add a player.room or use current.room in program
# - start building out player class

