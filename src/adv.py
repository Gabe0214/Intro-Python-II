from room import Room
from player import Player


# Declare all the rooms






room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
person = Player(input("Please insert your name: "), room['outside'])

# print(person.current_room)
# person.change_current_room(person.current_room.n_to)
# print(person.current_room)

def try_again():
    print("You ran into a trap. It's game over")
    start()


def print_info():
    print(person.current_room.user)

def start():
    print(f"Hello, {person.user} You are standing {person.current_room}")
    navigate = ""
    while navigate !=  'q':
        navigate = input("Where should you go?(n, s, e, w to Navigate or q to quit): ")
        if navigate == "n":
            if person.current_room.n_to is not None:
                person.change_current_room(person.current_room.n_to)
                print(f'You are now in {person.current_room}')
            else:
                print("opps")
                try_again()
        if navigate == "e":
            if person.current_room.e_to is not None:
                 person.change_current_room(person.current_room.e_to)
                 print(f'You are now in {person.current_room}')
            else:
                try_again()
        if navigate == "s":
            if person.current_room.s_to is not None:
                person.change_current_room(person.current_room.s_to)
                print(f'You are now in {person.current_room}')
            else: 
                try_again()
        if navigate =="w":
             if person.current_room.w_to is not None:
                 person.change_current_room(person.current_room.w_to)
                 print(f"You are in {person.current_room}")
             else: 
                 try_again()
        elif navigate == 'q':
            print("You have quit the game")        
    
        



start()


    

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
