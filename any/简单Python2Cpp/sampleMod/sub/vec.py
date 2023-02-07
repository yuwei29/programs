import subsub.add
def vecDot(x,y):
    l=len(x)
    sum=0
    for i in range(l):
        sum+=x[i]*y[i]
    return sum