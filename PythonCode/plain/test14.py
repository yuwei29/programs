s=''
import random 
import string
slen = int(3e5)
alphas = 'abcdefghijklmnopqrstuvwxyz'
for i in range(slen):
    s+=random.choice(alphas)
print('start')
m=int(1e9+7)

L = len(s)
def ok(i,j,k):
    if i==j and j!=k:
        return True
    elif i==k and i!=j:
        return True
    elif j==k and i!=j:
        return True
    return False
g=dict()
chrcnts = dict()

for i in alphas:
    chrcnts[i]=0
    for j in alphas:
        g[(i,j)]=0
def f(n):
    cnt=0
    chrcnts[s[0]]=1
    if n<2:
        return 0
    for i in range(2,n+1):
        for k in g:
            if ok(k[0],k[1],s[i-1]):
                cnt+=g[k]
        cnt%=m
        # for j in range(i-1):    complexity O(n), which is too big 
        #     g[(s[j],s[i-1])]+=1
        for k in chrcnts:
            g[(k,s[i-1])]+=chrcnts[k]
        chrcnts[s[i-1]]+=1
        
    # if n<20:
    #     for i in range(L-2):
    #         for j in range(i+1,L-1):
    #             for k in range(j+1,L):
    #                 cnt+= ok(i,j,k)
    
    return cnt

print(f(L))