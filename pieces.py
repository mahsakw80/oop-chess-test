from abc import ABCMeta, abstractmethod
from main import ChessBoard
from player import Player


class Piece(metaclass=ABCMeta):
    def __init__(self, player, loc):
        if not isinstance(player, Player):
            raise Exception
        self.loc = loc
        self.player = player
        self.relative_moves = []
        self.name_of_piece = ' '
        self.initial_configs()
        self.player_configs()

    @abstractmethod
    def initial_configs(self):
        pass

    def __repr__(self):
        return f"\033[33m{self.name_of_piece}\033[0m"

    def player_configs(self):
        if self.player == Player.WHITE:
            self.name_of_piece = self.name_of_piece.upper()

        elif self.player == Player.BLACK:
            self.name_of_piece = self.name_of_piece.lower()
            self.relative_moves = [(-x, -y) for x, y in self.relative_moves]

    def _possible_move(self, stop):
        file_start, rank_start = self.loc
        file_stop, rank_stop = stop

        for r, f in self.relative_moves:
            rank_condition = int(rank_stop) - int(rank_start) == r
            file_condition = ord(file_stop) - ord(file_start) == f
            if rank_condition and file_condition:
                return True

        return False

    def move(self, stop):
        if self._possible_move(stop):
            cb = ChessBoard()
            cb[self.loc] = '.'      
            cb[stop] = self
            self.loc = stop
            return True

        return False


class Pawn(Piece):
    def initial_configs(self):
        self.name_of_piece = 'P'
        self.relative_moves = [(1, 0), (2, 0)]


class Knight(Piece):
    def initial_configs(self):
        self.name_of_piece = 'N'
        self.relative_moves = [(1, 2), (1, -2), (2, 1), (2, -1),
                               (-1, 2), (-1, -2), (-2, -1), (-2, 1)]


class Bishop(Piece):
    def initial_configs(self):
        self.name_of_piece = 'B'
        relmov=[]
        for x in range(1,9):
            self.relative_moves.append((x,x))
            self.relative_moves.append((-x,x))
            self.relative_moves.append((x,-x))
            self.relative_moves.append((-x,-x))


class Rook(Piece):
    def initial_configs(self):
        self.name_of_piece = 'R'
        for x in range(1,9):
            self.relative_moves.append((0,x))
            self.relative_moves.append((0,-x))
            self.relative_moves.append((x,0))
            self.relative_moves.append((-x,0))


class Queen(Piece):
    def initial_configs(self):
        self.name_of_piece = 'Q'
        for x in range(1,9):
            self.relative_moves.append((0,x))
            self.relative_moves.append((0,-x))
            self.relative_moves.append((x,0))
            self.relative_moves.append((-x,0))
            self.relative_moves.append((x,x))
            self.relative_moves.append((-x,x))
            self.relative_moves.append((x,-x))
            self.relative_moves.append((-x,-x))


class King(Piece):
    def initial_configs(self):
        self.name_of_piece = 'K'
        self.relative_moves = [(1, 0), (-1, 0),(0,1),(-1,0)]