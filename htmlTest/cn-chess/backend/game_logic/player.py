from .pieces import getPieceMoves as PM, roles
import random
class Player:
    def __init__(self,color):
        self.color = color
        self.moves = []
        if color == 'black':
            self.pieces = [('Z0',(0,3)),('Z1',(2,3)),('Z2',(4,3)),('Z3',(6,3)),('Z4',(8,3)),
            ('P0',(1,2)),('P1',(7,2)),('C0',(0,0)),('M0',(1,0)),('X0',(2,0)),('S0',(3,0)),
            ('J0',(4,0)),('S1',(5,0)),('X1',(6,0)),('M1',(7,0)),('C1',(8,0))]
        else:
            self.pieces = [('z0',(0,6)),('z1',(2,6)),('z2',(4,6)),('z3',(6,6)),('z4',(8,6)),
            ('p0',(1,7)),('p1',(7,7)),('c0',(0,9)),('m0',(1,9)),('x0',(2,9)),('s0',(3,9)),
            ('j0',(4,9)),('s1',(5,9)),('x1',(6,9)),('m1',(7,9)),('c1',(8,9))]

    def getMoves(self,board):
        self.moves = []
        for p in self.pieces:
            role = roles[p[0][0].lower()]
            self.moves += PM(board,self.color,role,p[1][0],p[1][1])

    def play(self,mode,board):
        self.getMoves(board)
        if len(self.moves)==0:
            return [-1,-1,-1,-1]
        if mode=='random':
            choice = random.randint(0,len(self.moves)-1)
            return self.moves[choice]
