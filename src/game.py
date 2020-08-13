MOVE_N = 'n'
MOVE_S = 's'
MOVE_E = 'e'
MOVE_W = 'w'

DIRECTIONS = [MOVE_N, MOVE_S, MOVE_E, MOVE_W]

QUIT = 'q'



def parse(command):
    command, *args = command.split(' ')
    return command, args


class Game:

    __slots__ = ['__rooms', '__player']

    def __init__(self, rooms, player):
        self.__rooms = rooms
        self.__player = player

    @property
    def player(self):
        return self.__player

    @property
    def rooms(self):
        return self.__rooms

    def move_player(self, direction):
        if direction == MOVE_N and (north := self.__player.current_room.n_to):
            self.__player.move(north)
        elif direction == MOVE_S and (south := self.__player.current_room.s_to):
            self.__player.move(south)
        elif direction == MOVE_E and (east := self.__player.current_room.e_to):
            self.__player.move(east)
        elif direction == MOVE_W and (west := self.__player.current_room.w_to):
            self.__player.move(west)

    def tick(self, command):
        command, args = parse(command)
        if (direction := command) in DIRECTIONS:
            self.move_player(command)
