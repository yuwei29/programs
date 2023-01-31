n=int(input())
xs=dict()
ys=dict()
xys=dict()
score=0
for i in range(n):
    x,y=map(int,input().split())
    if x in xs:
        score+=xs[x]
        xs[x]+=1
    else:
        xs[x]=1
    if y in ys:
        score+=ys[y]
        ys[y]+=1
    else:
        ys[y]=1
    if (x,y) in xys:
        score-=xys[(x,y)]
        xys[(x,y)]+=1
    else:
        xys[(x,y)]=1
print(score)


