'''  '''
n,k=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
def bi(x,l,r):
    if x>a[r] or x<a[l]:
        return -1
    mid=(l+r)//2
    if x>=a[mid] and (mid==n-1 or x<a[mid+1]):
        return mid
    elif x<a[mid]:
        return bi(x,l,mid-1)
    else:
        return bi(x,mid+1,r)
ans=0
for i in range(n):
    r = bi(a[i]+k,i,n-1)
    ans=max(ans,r-i+1)
print(ans)