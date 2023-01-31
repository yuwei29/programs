'''
gonna write some policy evaluation and improvement program
state = [[x1,...,...],[y1,...,...],[z1,...,...]]
def policy(color):
  decide player according to color
  getLegalMoves
  for move in moves:
    isend(move)
    win:1
    lose:-1
    tie:0
    others : gamma*value(s') 
 update value #value is a NN that maps state-representation to float number 
  return move with highest score

'''
import random
import torch
from model import updateModel
from model import value
class State:
    def __init__(self,board):
        self.end=False
        self.score=0
        self.board=board
def getMoves(s):
    legalMoves=[]
    for i in range(3):
        for j in range(3):
            if s.board[i][j]==0:
                legalMoves.append((i,j))
    return legalMoves
                
def updateState(s,color,move):
    board = s.board.detach().clone()
    s1 = State(board)
    if color=='black':
        s1.board[move[0]][move[1]]=1
    else:
        s1.board[move[0]][move[1]]=-1
    for i in range(3):
        cnt=0
        for j in range(3):
            cnt+=s1.board[i][j]
        if cnt==3 or cnt==-3:
            s1.end=True
            s1.score=1
            return s1
    for i in range(3):
        cnt=0
        for j in range(3):
            cnt+=s1.board[j][i]
        if cnt==3 or cnt==-3:
            s1.end=True
            s1.score=1
            return s1
    a=s1.board[0][0]+s1.board[1][1]+s1.board[2][2]
    b=s1.board[2][0]+s1.board[1][1]+s1.board[0][2]
    if abs(a)==3 or abs(b)==3:
        s1.end=True
        s1.score=1
        return s1
    cnt=0
    for i in range(3):
        for j in range(3):
            cnt+= (s1.board[i][j]!=0)
    if cnt==9:
        s1.end = True
    return s1
def game(mode):
    board=torch.zeros(3,3)
    s=State(board)
    gamma = 0.2
    steps=[]
    while True:
        color = 'black'
        if mode=='greedy':
            move = policy_greedy(color,s,gamma,True)
        elif mode=='strict':
            move = policy_greedy(color,s,gamma,False)
        else:
            move = policy_random(color,s)
        steps.append((color,move))
        s = updateState(s,color,move)
        if s.end:
            if s.score == 1:
                return 'black',s.board,steps
            else:
                return 'tie',s.board,steps
            # print(steps)
            # print(s.board)
            # return
        color = 'white'
        if mode=='greedy':
            move = policy_greedy(color,s,gamma,True)
        elif mode=='strict':
            move = policy_greedy(color,s,gamma,False)
        else:
            move = policy_random(color,s)
        steps.append((color,move))
        s = updateState(s,color,move)
        if s.end:
            if s.score == 1:
                #print("white wins")
                return 'white',s.board,steps
            else:
                #print("tie")
                return 'tie',s.board,steps
            # print(steps)
            # print(s.board)
            
        

    
def policy_greedy(color,s,gamma,explore):
    moves = getMoves(s)
    maxScore = -1.01
    for move in moves:
        s2 = updateState(s,color,move)
        if s2.end:
            score=s2.score
        else:
            board = torch.reshape(s2.board,(-1,9))
            board = board.detach().clone()
            score=gamma*value(board,color)
        if score>maxScore:
            maxScore = score
            bestAction = move
    board = torch.reshape(s.board,(-1,9))
    board = board.detach().clone()
    
    if explore:
        magic = random.randint(1,5) # e-greedy with e = 0.2
        if magic==3 and maxScore < 1 and maxScore != 0:
            bestAction = moves[random.randint(0,len(moves)-1)]
            s2 = updateState(s,color,bestAction)
            tmp = torch.reshape(s2.board,(-1,9))
            tmp = tmp.detach().clone()
            maxScore = gamma*value(tmp,color)
    newValue = torch.tensor(maxScore,dtype=torch.float)
    updateModel(color,board,newValue)
    return bestAction

def policy_random(color,s):
    moves = getMoves(s)
    bestAction = (-1,-1)
    for move in moves:
        s2 = updateState(s,color,move)
        if s2.end:
            bestAction = move
            break
    if bestAction[0]==-1:
        L = len(moves)
        bestAction = moves[random.randint(0,L-1)]
    return bestAction