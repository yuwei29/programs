import sub.trans
import sub.vec
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
    y=sub.trans.transpose(y)
    for i in range(row):
        for j in range(col):
            res[i][j]=sub.vec.vecDot(x[i],y[j])
    return res
