n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())

if x==0:
    print('infinity')
    exit(0)
a.sort()
if y>0:
    print(a[y]-a[y-1])
else:
    print(a[0])