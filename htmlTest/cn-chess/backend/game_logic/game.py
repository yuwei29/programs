from .player import Player
from .board import init_board
def update(act,p1,p2,board):
    '''p1 active, p2 inactive'''
    peace=True
    winner = None
    x,y,nx,ny = act
    if x==-1:
        return False,p2.color
    piece = board[y][x]
    board[y][x]=0
    if board[ny][nx]!=0:
        peace=False
        p2.pieces.remove((board[ny][nx],(nx,ny)))
        if board[ny][nx]=='j0':
            winner = 'black'
        elif board[ny][nx]=='J0':
            winner = 'red'
    board[ny][nx]=piece
    p1.pieces.remove((piece,(x,y)))
    p1.pieces.append((piece,(nx,ny)))
    return peace,winner

def run():
    board = init_board()
    p1 = Player('red')
    p2 = Player('black')
    peaceCount = 0
    while peaceCount < 60:
        act = p1.play('random',board)
        peace,winner = update(act,p1,p2,board)
        if winner!=None:
            break
        if peace:
            peaceCount+=1
        else:
            peaceCount=0
        act = p2.play('random',board)
        peace,winner = update(act,p2,p1,board)
        if winner!=None:
            break
        if peace:
            peaceCount+=1
        else:
            peaceCount=0
    print(board)
    return winner

if __name__ == '__main__':
    run()