n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in range(n):
	for j in range(i+1,n+1):
	   ans=max(ans,sum(a[i:j]))
print(ans)