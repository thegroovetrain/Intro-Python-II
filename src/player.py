# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    __slots__ = ['__name', '__room']

    def __init__(self, name, current_room):
        self.__name = name
        self.__room = current_room

    def __str__(self):
        return f'<Player> {self.__name}'

    @property
    def name(self):
        return self.__name

    @property
    def current_room(self):
        return self.__room

    def move(self, room):
        self.__room = room
