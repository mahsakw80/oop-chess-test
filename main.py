#from pieces import King, Knight, Bishop, Rook, Pawn, Queen
from player import Player

from abc import ABCMeta, abstractmethod

FILES = "abcdefgh"
RANKS = "12345678"


class Piece(metaclass=ABCMeta):
    def __init__(self, player, loc):
        if not isinstance(player, Player):
            raise Exception
        self.loc = loc
        self.player = player
        self.relative_moves = []
        self.name_of_piece = ' '
        self.lock=False
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
            for item in self.relative_moves:
                for x in item:
                    x[0]*=-1
                    x[1]*=-1

            # for i in range(len(self.relative_moves)):
            #     reflex+=[(-x, -y) for x, y in self.relative_moves[i]]
            # self.relative_moves=[reflex]
            #self.relative_moves = [(-x, -y) for x, y in self.relative_moves]
    def distance_convertor(self,nowloc,movelist,board):
        result=[]
        f=FILES.index(nowloc[0])
        r=RANKS.index(nowloc[1])
        for item in movelist:
            ff=f+item[1]
            rr=r+item[0]
            if -1<ff<8 and -1<rr<8:
                fchar=FILES[ff]
                rnum=RANKS[rr]
                fr=fchar+rnum
                
                if board[nowloc].isupper():
                    if board[fr]==".":
                        if board[nowloc]=="P" :
                            if item in [(1,1),(1,-1)]:
                                continue
                            else:
                                result.append(fr)

                        else:
                            result.append(fr)
                    elif board[fr].islower() :
                        if board[nowloc]=="P" :
                            if item in [(1,0),(2,0)]:
                                break
                            else:result.append(fr)
                        else:
                            result.append(fr)
                            break
                    elif board[fr].isupper() :
                        break
                if board[nowloc].islower():
                    if board[fr]==".":
                        if board[nowloc]=="p" :
                            if item in [(-1,1),(-1,-1)]:
                                continue
                            else:result.append(fr)
                        else:result.append(fr)
                    elif board[fr].isupper() :
                        if board[nowloc]=="p" :
                            if item in [(-1,0),(-2,0)]:
                                break
                            else:
                                result.append(fr)
                        else:
                            result.append(fr)
                            break
                    elif board[fr].islower() :
                        break
        return result        



        pass      
    def masir(self,brd):
        possible=[]
        for item in self.relative_moves:
          if [self.distance_convertor(self.loc,item,brd)]!=[]:
            possible+=[self.distance_convertor(self.loc,item,brd)]
        if self.name_of_piece=='p' or  self.name_of_piece=='P' :
            possible.remove(possible[0])
        return possible
          

    def _possible_move(self, stop,mvlst,nloc,brd):
        possible=[]
        fs,rs=stop
        fn,rn=nloc
        rr=int(rs)-int(rn)
        ff=ord(fs)-ord(fn)
        if brd[nloc]=='P' :
            if (rr,ff)==(2,0):
                if stop  not in ['a4','b4','c4','d4','e4','f4','g4','h4']:
                    return False
            if (rr,ff)==(1,1) or (rr,ff)==(1,-1):
                if brd[stop].islower():
                    return True
                return False

        if brd[nloc]=='p':
            if (rr,ff)==(-2,0):    
                if stop not in ['a5','b5','c5','d5','e5','f5','g5','h5']:
                    return False
            if (rr,ff)==(-1,-1) or (rr,ff)==(-1,1):
                if brd[stop].isupper():
                    return True
                return False

            
        for item in mvlst:
            possible+=self.distance_convertor(nloc,item,brd)
        if stop in possible:
            return True
        else:return False    
        # file_start, rank_start = self.loc
        # file_stop, rank_stop = stop
        # move_list=None
        # f=ord(file_stop) - ord(file_start)
        # r=int(rank_stop) - int(rank_start)
        # knight_move=self.relative_moves.get("move")
        # if knight_move==None:
        #     if abs(f)==abs(r):
        #         if f>0 and r>0:
        #             move_list=self.relative_moves.get("rightup")
        #         if f>0 and r<0:
        #             move_list=self.relative_moves.get("rightdown")
        #         if f<0 and r>0:
        #             move_list=self.relative_moves.get("leftup")
        #         if f<0 and r<0:
        #             move_list=self.relative_moves.get("leftdown")
        #     if f==0 and r>0:
        #         move_list=self.relative_moves.get("up")
        #     if f==0 and r<0:
        #         move_list=self.relative_moves.get("down")
        #     if f>0 and r==0:
        #         move_list=self.relative_moves.get("right")
        #     if f<0 and r==0:
        #         move_list=self.relative_moves.get("left")
            # move_list.index()    
            

            # pass


        # for r, f in self.relative_moves:
        #     rank_condition = int(rank_stop) - int(rank_start) == r
        #     file_condition = ord(file_stop) - ord(file_start) == f
        #     if rank_condition and file_condition:
        #         return True

        return False

    def move(self, stop,location):
        if self._possible_move(stop,self.relative_moves,self.loc,location):
            cb = ChessBoard()
            cb[self.loc] = '.'      
            cb[stop] = self
            self.loc = stop
            return True

        return False


class Pawn(Piece):
    def initial_configs(self):
        self.name_of_piece = 'P'
        self.relative_moves = [[[1, 0],[2, 0]],[[1,1]],[[1,-1]]]
        self.lock=True


class Knight(Piece):
    def initial_configs(self):
        self.name_of_piece = 'N'
        self.relative_moves =[[[1, 2]], [[1, -2]], [[2, 1]], [[2, -1]],
                               [[-1, 2]], [[-1, -2]], [[-2, -1]], [[-2, 1]]]


class Bishop(Piece):
    def initial_configs(self):
        self.name_of_piece = 'B'
        self.relative_moves=[[[x,x]for x in range(1,9)],[[-x,x]for x in range(1,9)],
                             [[x,-x]for x in range(1,9)],[[-x,-x]for x in range(1,9)]]
        # relmov=[]
        # for x in range(1,9):
        #     self.relative_moves.append((x,x))
        #     self.relative_moves.append((-x,x))
        #     self.relative_moves.append((x,-x))
        #     self.relative_moves.append((-x,-x))


class Rook(Piece):
    def initial_configs(self):
        self.name_of_piece = 'R'
        self.relative_moves=[[[x,0]for x in range(1,9)],[[-x,0]for x in range(1,9)],
                             [[0,x]for x in range(1,9)],[[0,-x]for x in range(1,9)]]
        # for x in range(1,9):
        #     self.relative_moves.append((0,x))
        #     self.relative_moves.append((0,-x))
        #     self.relative_moves.append((x,0))
        #     self.relative_moves.append((-x,0))


class Queen(Piece):
    def initial_configs(self):
        self.name_of_piece = 'Q'
        self.relative_moves=[[[x,0]for x in range(1,9)],[[-x,0]for x in range(1,9)],
                             [[0,x]for x in range(1,9)],[[0,-x]for x in range(1,9)],[[x,x]for x in range(1,9)],[[-x,x]for x in range(1,9)],
                             [[x,-x]for x in range(1,9)],[[-x,-x]for x in range(1,9)]]
        # for x in range(1,9):
        #     self.relative_moves.append((0,x))
        #     self.relative_moves.append((0,-x))
        #     self.relative_moves.append((x,0))
        #     self.relative_moves.append((-x,0))
        #     self.relative_moves.append((x,x))
        #     self.relative_moves.append((-x,x))
        #     self.relative_moves.append((x,-x))
        #     self.relative_moves.append((-x,-x))


class King(Piece):
    def initial_configs(self):
        self.name_of_piece = 'K'
        self.relative_moves = [[[1, 0]], [[-1, 0]],[[0,1]],[[0,-1]]]



class ChessBoard:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.is_initiated = False

        return cls._instance

    def __init__(self):
        if not self.is_initiated:
            self.is_initiated = True
            self.loclist=["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8",
                          "c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8",
                          "e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8",
                          "g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]
            self.location={"a1":"R","a2":"P","a3":".","a4":".","a5":".","a6":".","a7":"p","a8":"r",
                           "b1":"N","b2":"P","b3":".","b4":".","b5":".","b6":".","b7":"p","b8":"n",
                           "c1":"B","c2":"P","c3":".","c4":".","c5":".","c6":".","c7":"p","c8":"b",
                           "d1":"Q","d2":"P","d3":".","d4":".","d5":".","d6":".","d7":"p","d8":"q",
                           "e1":"K","e2":"P","e3":".","e4":".","e5":".","e6":".","e7":"p","e8":"k",
                           "f1":"B","f2":"P","f3":".","f4":".","f5":".","f6":".","f7":"p","f8":"b",
                           "g1":"N","g2":"P","g3":".","g4":".","g5":".","g6":".","g7":"p","g8":"n",
                           "h1":"R","h2":"P","h3":".","h4":".","h5":".","h6":".","h7":"p","h8":"r",}
            self.turn = Player.WHITE
            self.__chess_board = {rank: {file: '.' for file in FILES} for rank in RANKS}
            self.__chess_board['2'] = {file: Pawn(Player.WHITE, f"{file}2") for file in FILES}
            self.__chess_board['7'] = {file: Pawn(Player.BLACK, f"{file}7") for file in FILES}
            self.__chess_board['1'] = {
                'a': Rook(Player.WHITE, 'a1'),
                'b': Knight(Player.WHITE, 'b1'),
                'c': Bishop(Player.WHITE, 'c1'),
                'd': Queen(Player.WHITE, 'd1'),
                'e': King(Player.WHITE, 'e1'),
                'f': Bishop(Player.WHITE, 'f1'),
                'g': Knight(Player.WHITE, 'g1'),
                'h': Rook(Player.WHITE, 'h1')
            }
            self.__chess_board['8'] = {
                'a': Rook(Player.BLACK, 'a8'),
                'b': Knight(Player.BLACK, 'b8'),
                'c': Bishop(Player.BLACK, 'c8'),
                'd': Queen(Player.BLACK, 'd8'),
                'e': King(Player.BLACK, 'e8'),
                'f': Bishop(Player.BLACK, 'f8'),
                'g': Knight(Player.BLACK, 'g8'),
                'h': Rook(Player.BLACK, 'h8')
            }

    def __repr__(self):
        text = ""
        for rank in self.__chess_board:
            line = " ".join(map(str, self.__chess_board[rank].values()))

            text = f"\033[31;1m{rank:<2}\033[0m{line}\n{text}"

        text += "  \033[32;2ma b c d e f g h\033[0m"
        return text

    def move_piece(self, start, stop):
        if self.turn == Player.BLACK and self[start].name_of_piece.isupper():
            raise Exception

        if self.turn == Player.WHITE and self[start].name_of_piece.islower():
            raise Exception

        # self[stop] = self[start]
        # self[start] = "."
        change=self[start].move(stop,self.location)
        if change:
            self.location[stop]=self.location[start]
            self.location[start]='.'  
            if self.kish:
                return 'kish'
        self.turn = Player.BLACK if self.turn == Player.WHITE else Player.WHITE
        return change

    def msr(self,start):
        psblmv=self[start].masir(self.location)
        return psblmv 
    def result(self,lst):
        rs=[]
        for x in lst:
                for y in x:
                    for z in y:
                        rs.append(z)
        return rs          
    def kngcheck(self,toplst,kngloc):
        for item in toplst:
                if kngloc in item:
                    return item
        return False    
    def kinglocation(self,witch):

        for x in self.loclist:
            if self.location[x]==witch:
                return x
                        
                  
    def allmasir(self,witch,kingloc):
        urs=[]
        lrs=[]
        kng=[]
        ku=[]
        kl=[]
        for loc in self.loclist:
            if self.location[loc]=="k" and witch=='u':
                kingloc=loc
            if self.location[loc]=="K" and witch=='l':
                kingloc=loc
        for loc in self.loclist:
            if self.location[loc].isupper():
                a=self.msr(loc)
                b=self.kngcheck(a,kingloc)
                if b!=False:
                    ku=[[loc]+b]
                # if witch=='u':
               # rslt.append(loc)

                urs.append(a)
                # elif witch=='l':
            elif self.location[loc].islower():    
                a=self.msr(loc)
                b=self.kngcheck(a,kingloc)
                if b!=False:
                    kl=[[loc]+b]
                lrs.append(a)    
                #print(self.msr(loc))
            #rs+=[rslt]
        if witch=='u':
            return self.result(urs) ,ku   
        elif witch=='l':
            return self.result(lrs),kl    
    def kingmove(self,start):
        b=[]
        a=self.msr(start)
        for item in a:
            for x in item:
                b.append(x)
        return b    
    def kish(self):
        kish=False
        mat=False
        bigking=self.kinglocation('K')
        smallking=self.kinglocation('k')
        allmsrbig,posb=self.allmasir('u',smallking)
        allmsrsmall,poss=self.allmasir('l',bigking)
        # allmsrbig+=self.kingmove(bigking)
        # allmsrsmall+=self.kingmove(smallking)
        for item in allmsrbig:
            if item==smallking:
                kish=True
        for item in allmsrsmall:
            if item==bigking:
                kish=True
        # print(allmsrbig,'\n\n\n',allmsrsmall,'\n')
        # print(bigking,'\n\n\n',smallking)
        # if kish==True: 
        #     for item in poss:
        #         if item not in allmsrbig:
        #             mat=True
        #     for item in posb:
        #         if item not in allmsrsmall:
        #             mat=True
        return kish
    # def mat(self):
    #     if self.kish==True:
    #         allmovebig,atac_b=self.kinglocation('K')
    #         allmovesmall,atac_s=self.kinglocation('k')
    #         i=0
    #         for item in atac_b:
    #             for x in item:
    #                 if x in allmovesmall:
    #                     atac_b.remove(item)
                
    #     print(atac_b)     
                

    def __getitem__(self, loc: str):
        file, rank = loc
        return self.__chess_board[rank][file]

    def __setitem__(self, loc, value):
        file, rank = loc
        self.__chess_board[rank][file] = value


chess_board = ChessBoard()
# print(chess_board)
# while True:
#     a=input('sth...')
#     b=input('sth...')
#     if a=='ex':
#         break
#     chess_board.move_piece(a,b)
#     print(chess_board)


