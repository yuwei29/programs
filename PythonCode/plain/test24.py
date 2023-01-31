'''
Ax = b  
let |Ax-b| be the distance of x to accurate solution
'''
def axmul(a,b):
    res=[]
    l=len(b)
    for v in a:
        res.append(sum([v[i]*b[i] for i in range(l)]))
    return res
def vsub(a,b):
    return [a[i]-b[i] for i in range(len(a))]
def l2(a):
    return sum([e*e for e in a])
def f(a,b):
    def g(x):
        return l2(vsub(axmul(a,x),b))
    return g
a=[[4,1],[1,3]]
b=[1,2]
g=f(a,b)
def main():
    a=[[4,1],[1,3]]
    b=[1,2]
    g=f(a,b)

    c=[[0,0],[-1,-1],[-1,0],[0,-1],[0,0.5],[0.5,0],[0.5,0.5]]
    for e in c:
        print(g(e))

#main()