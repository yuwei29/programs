def f(a):
    l=[]
    for i in range(32):
        l.append(a%2)
        a//=2
    ans = 0
    bns=0
    for i in range(31,15,-1):
        ans=ans*2+l[i]
    for i in range(15,-1,-1):
        bns=bns*2+l[i]
    ans = 1024*64*bns+ans
    return ans
print(f(1314520))