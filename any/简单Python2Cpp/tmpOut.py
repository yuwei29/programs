def transpose(x):
    r=len(x)
    c=len(x[0])
    res=[[0]*r for i in range(c)]
    for i in range(c):
        for j in range(r):
            res[i][j]=x[j][i]
    return res
def add3(x,y,z):
  return x+y+z
def vecDot(x,y):
    l=len(x)
    sum=0
    for i in range(l):
        sum+=x[i]*y[i]
    return sum
def matMul(x,y):
    res=[]
    row=len(x)
    col=len(y[0])
    d=len(y)
    for i in range(row):
        tmp=[]
        for j in range(col):
            sum=0
            for k in range(d):
                sum+=x[i][k]*y[k][j]
            tmp.append(sum)
        res.append(tmp)
    return res

def matMul2(x,y):
    row=len(x)
    col=len(y[0])
    res=[[0]*col for i in range(row)]
    y=trans.transpose(y)
    for i in range(row):
        for j in range(col):
            res[i][j]=vec.vecDot(x[i],y[j])
    return res

