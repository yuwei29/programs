def transpose(x):
    r=len(x)
    c=len(x[0])
    res=[[0]*r for i in range(c)]
    for i in range(c):
        for j in range(r):
            res[i][j]=x[j][i]
    return res