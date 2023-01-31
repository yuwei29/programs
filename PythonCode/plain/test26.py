n,k=map(int,input().split())
a=list(map(int,input().split()))
from math import sqrt
def isp(x):
    if x==1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0:
        return False
    m=int(sqrt(x))
    for i in range(3,m+1):
        if x%i==0:
            return False
    return True
    
def f(a,k):
    l=len(a)
    res=[]
    if l==0 or k==0 or l<k:
        return [0]
    for i in range(l-k+1):
        pre=a[i]
        res+=[pre+e for e in f(a[i+1:],k-1)]
    return res

#import sys
#sys.setrecursionlimit(123456)
v=f(a,k)
ans=sum([isp(e) for e in v])
print(ans)