''' 终于放假了。小A决定在假期期间出去旅游。她提前拟定了许多旅游路线，但预算只允许她选取三条路线旅游。每条旅游路线会占用一段连续日期。
在小A选择的所有路线中，任意两条路线所占用的日期不能有重叠部分。现在她想知道有多少种选择三条互不冲突的路线的方案可以供她选择？



输入描述
第一行有一个正整数n(3<=n<=100000)，代表小A拟定的路线数量。

第二行有n个正整数，第i个代表第i条路线的起始日期。

第三行有n个正整数，第i个代表第i条路线的终止日期。

输入保证起始日期不晚于终止日期。日期最大不超过1000000000。

输出描述
输出一个非负整数，代表所求的答案。


样例输入
6
4 1 3 2 1 2 
4 1 3 3 2 2
样例输出
6 '''
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[(0,0)]
c+=[(a[i],b[i]) for i in range(n)]
s=[0]*100005
def bi(i,l,r):
    if s[i]!=0:
        return s[i]
    t=c[i][1]
    mid=(l+r)//2
    if c[r][0]<=t:
        return -1
    if c[mid][0]>t and (mid==l or c[mid-1][0]<=t):
        s[i]=mid
        return mid
    elif c[mid][0]<=t:
        return bi(i,mid+1,r)
    else:
        return bi(i,l,mid-1)

def f(x):
    return x[0]
c.sort(key=f)
ans=0
for i in range(n-2):
    j=bi(i,i+1,n-2)
    if j>=0:
        for k in range(j,n-1):
            t=bi(k,k+1,n-1)
            if t>=0:
                ans+=n-t
print(ans)