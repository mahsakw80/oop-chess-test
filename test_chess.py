import pytest
from main import ChessBoard


class Testchess:
    @pytest.fixture
    def setUp(self):
        self.chess=ChessBoard()
        yield 'Done ...'
    
    def test_pawn(self):
        self.chess=ChessBoard()
        #two
        assert self.chess.move_piece("a2","a4")==True
        assert self.chess.move_piece("h7","h5")==True
        assert self.chess.move_piece("a4","a6")==False
        assert self.chess.move_piece("h5","h3")==False
        #one
        assert self.chess.move_piece("e2","e3")==True
        assert self.chess.move_piece("f7","f5")==True
        assert self.chess.move_piece("e3","f4")==False
        assert self.chess.move_piece("f5","g4")==False
    def test_rock(self):
        self.chess=ChessBoard()
        assert self.chess.move_piece("d2","d4")==True
        assert self.chess.move_piece("h8","h6")==True
        assert self.chess.move_piece("a1","a3")==True
        assert self.chess.move_piece("d7","d5")==True
        assert self.chess.move_piece("a3","b3")==True
        assert self.chess.move_piece("h6","f6")==True
    def test_bishop(self) :
        self.chess=ChessBoard()
        assert self.chess.move_piece("f1","c4")==True
        assert self.chess.move_piece("c8","e6")==True
        assert self.chess.move_piece("c4","c5")==False
        assert self.chess.move_piece("e6","e5")==False
    def test_knigth(self):
        self.chess=ChessBoard()
        assert self.chess.move_piece("g1","h3")==True
        assert self.chess.move_piece("b8","a6")==True
        assert self.chess.move_piece("h3","h2")==False
        assert self.chess.move_piece("a6","a5")==False
    def test_king(self):
        self.chess=ChessBoard()
        assert self.chess.move_piece("e1","d1")==False
        assert self.chess.move_piece("g7","g5")==True
        assert self.chess.move_piece("e1","e2")==True
        assert self.chess.move_piece("g5","g4")==True
    def test_queen(self):
        self.chess=ChessBoard()
        assert self.chess.move_piece("c2","c3")==True
        assert self.chess.move_piece("g4","g2")==False
        assert self.chess.move_piece("d1","c2")==True
    def test_kish(self):
        pass
        # self.chess=ChessBoard()
        # assert self.chess.move_piece("e6","g4")=='kish'























