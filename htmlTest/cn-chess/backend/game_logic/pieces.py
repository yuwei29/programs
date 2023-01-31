def getColor(x):
    if x==0:
        return None
    if x[0]>='A' and x[0]<='Z':
        return 'black'
    return 'red'

def getPieceMoves(board,color,role,x,y):
    moves = []
    limits=[[0,8],[0,9]]
    if role == 'zu':
        if color == 'black':
            if y<9 and 'black'!=getColor(board[y+1][x]):
                moves.append([x,y,x,y+1])
            if y>4:
                if x>0 and 'black'!=getColor(board[y][x-1]):
                    moves.append([x,y,x-1,y])
                if x<8 and 'black'!=getColor(board[y][x+1]):
                    moves.append([x,y,x+1,y])
        else:
            if y>0 and 'red'!=getColor(board[y-1][x]):
                moves.append([x,y,x,y-1])
            if y<5:
                if x>0 and color!=getColor(board[y][x-1]):
                    moves.append([x,y,x-1,y])
                if x<8 and color!=getColor(board[y][x+1]):
                    moves.append([x,y,x+1,y])
    elif role == 'pao':
        p=(x,y)
        for i in range(2):
            for j in range(2):
                if p[i]!=limits[i][j]:
                    if p[i]<limits[i][j]:
                        r = range(p[i]+1,limits[i][j]+1)
                    else:
                        r = range(p[i]-1,-1,-1)
                    others = 0
                    for k in r:
                        if i==0:
                            if board[y][k]==0 and others==0:
                                moves.append([x,y,k,y])
                            elif board[y][k]!=0 and others==0:
                                others=1
                            elif board[y][k]!=0:
                                if color!=getColor(board[y][k]):
                                    moves.append([x,y,k,y])
                                break
                        else:
                            if board[k][x]==0 and others==0:
                                moves.append([x,y,x,k])
                            elif board[k][x]!=0 and others==0:
                                others=1
                            elif board[k][x]!=0:
                                if color!=getColor(board[k][x]):
                                    moves.append([x,y,x,k])
                                break
    elif role == 'che':
        p=(x,y)
        for i in range(2):
            for j in range(2):
                if p[i]!=limits[i][j]:
                    if p[i]<limits[i][j]:
                        r = range(p[i]+1,limits[i][j]+1)
                    else:
                        r = range(p[i]-1,-1,-1)
                    for k in r:
                        if i==0:
                            if board[y][k]==0:
                                moves.append([x,y,k,y])
                            elif board[y][k]!=0:
                                if color!=getColor(board[y][k]):
                                    moves.append([x,y,k,y])
                                break
                        else:
                            if board[k][x]==0:
                                moves.append([x,y,x,k])
                            elif board[k][x]!=0:
                                if color!=getColor(board[k][x]):
                                    moves.append([x,y,x,k])
                                break
    elif role == 'ma':
        nexts = [[-2,-1],[-1,-2],[-2,1],[-1,2],[2,-1],[1,-2],[2,1],[1,2]]
        barriers = [[-1,0],[0,-1],[-1,0],[0,1],[1,0],[0,-1],[1,0],[0,1]]
        for i in range(8):
            newX = x+nexts[i][0]
            newY = y+nexts[i][1]
            bx = x+barriers[i][0]
            by = y+barriers[i][1]
            if 0<=newX<=8 and 0<=newY<=9 and board[by][bx]==0:
                if color!=getColor(board[newY][newX]):
                    moves.append([x,y,newX,newY])
    elif role == 'xiang':
        gong = [0,4]
        if color == 'red':
            gong = [5,9]
        nexts = [[-2,-2],[-2,2],[2,-2],[2,2]]
        barriers = [[-1,-1],[-1,1],[1,-1],[1,1]]
        for i in range(4):
            newX = x+nexts[i][0]
            newY = y+nexts[i][1]
            bx = x+barriers[i][0]
            by = y+barriers[i][1]
            if 0<=newX<=8 and gong[0]<=newY<=gong[1] and board[by][bx]==0:
                if color!=getColor(board[newY][newX]):
                    moves.append([x,y,newX,newY])
    elif role == 'shi':
        gong = [0,2]
        if color == 'red':
            gong = [7,9]
        nexts = [[-1,-1],[-1,1],[1,-1],[1,1]]
        for i in range(4):
            newX = x+nexts[i][0]
            newY = y+nexts[i][1]
            if 3<=newX<=5 and gong[0]<=newY<=gong[1]:
                if color!=getColor(board[newY][newX]):
                    moves.append([x,y,newX,newY])
    else:
        gong = [0,2]
        if color == 'red':
            gong = [7,9]
            r = range(y-1,-1,-1)
        else:
            r = range(y+1,10)
        nexts = [[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(4):
            newX = x+nexts[i][0]
            newY = y+nexts[i][1]
            if 3<=newX<=5 and gong[0]<=newY<=gong[1]:
                if color!=getColor(board[newY][newX]):
                    moves.append([x,y,newX,newY])
        for k in r:
            if board[k][x]!=0:
                if board[k][x]=='j0' or board[k][x]=='J0':
                    moves.append([x,y,x,k])
                break
    return moves

roles = {'z':'zu','p':'pao','c':'che','m':'ma','x':'xiang','s':'shi','j':'jiang'}