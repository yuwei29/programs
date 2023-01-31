n,k = map(int,input().split())
s=input()
t='mihoyo'

for l in range(6*k,n+1):
    for i in range(n-l+1):
        if s[i:i+6]==t and s[i+l-6:i+l]==t:
            cnt=1
            for j in range(i+6,i+l-5):
                cnt += s[j:j+6]==t
            if cnt==k:
                print(i,i+l-1)
                exit(0)

print(-1)

