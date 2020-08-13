# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    __slots__ = ['__name', '__description', '__exits']

    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__exits = {
            'n_to': None,
            's_to': None,
            'e_to': None,
            'w_to': None
        }

    def __str__(self):
        return f'<Room> {self.__name}'

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def exits(self):
        return self.__exits

    @property
    def n_to(self):
        return self.__exits['n_to'] or None

    @n_to.setter
    def n_to(self, room):
        self.__exits['n_to'] = room

    @property
    def s_to(self):
        return self.__exits['s_to'] or None

    @s_to.setter
    def s_to(self, room):
        self.__exits['s_to'] = room

    @property
    def e_to(self):
        return self.__exits['e_to'] or None

    @e_to.setter
    def e_to(self, room):
        self.__exits['e_to'] = room

    @property
    def w_to(self):
        return self.__exits['w_to'] or None

    @w_to.setter
    def w_to(self, room):
        self.__exits['w_to'] = room
