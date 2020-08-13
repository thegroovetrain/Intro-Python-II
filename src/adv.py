from room import Room
from player import Player
from game import QUIT, Game
import os


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light 
flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied 
by earlier adventurers. The only exit is to the south."""),
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


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def get_player_input(prompt):
    return input(f'{prompt} > ')


def start_new_game():
    message = '*  WELCOME TO LAMBDA ADVENTURES!  *'
    spreader = ''.join(['*' for x in range(len(message))])
    print(spreader)
    print(message)
    print(spreader, '\n')
    name = get_player_input('What is your name, brave warrior?')

    rooms = setup_rooms()
    player = Player(name, rooms['outside'])

    return rooms, player


def display_room_description(player):
    name = f'* The Adventures of {player.name} *'
    name_spreader = ''.join(['*' for x in range(len(name))])
    print(name_spreader)
    print(name)
    print(name_spreader, '\n')

    print(player.current_room.name)
    print('-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-')
    print(player.current_room.description, '\n')


def main():

    message = '*  WELCOME TO LAMBDA ADVENTURES!  *'
    spreader = ''.join(['*' for x in range(len(message))])
    print(spreader)
    print(message)
    print(spreader, '\n')
    name = get_player_input('What is your name, brave warrior?')

    game = Game(room, Player(name, room['outside']))

    while True:
        clear()

        display_room_description(game.player)

        player_input = get_player_input('What shall you do?')

        if player_input == QUIT:
            break

        game.tick(player_input)

    clear()
    print('~ Thank you for playing! ~')


main()
