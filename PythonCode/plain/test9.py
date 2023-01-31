'''米小游有一棵有根树，树上共有n个节点。
米小游指定了一个节点x为根，然后定义所有相邻的、编号奇偶性相同的节点为一个连通块。米小游想知道，所有子树（共有n个子树）的连通块数量之和是多少？
举个例子：'''

'''如上图，3号节点被指定为根
然后3-1-5作为一个连通块，4号节点和2号节点为单独的连通块。
那么1号节点到5号节点，每个节点的子树连通块数量分别为：2、1、3、1、1，总连通块数量是8。

input:
5 3
1 2
1 3
3 4
5 1

output:
8'''

n,root = map(int,input().split())
g = dict()
for i in range(n-1):
    a,b = map(int,input().split())
    if a in g:
        g[a].append(b)
    else:
        g[a]=[b]
    if b in g:
        g[b].append(a)
    else:
        g[b]=[a]

def pure(root,pre):
    if pre in g[root]:
        g[root].remove(pre)
    for node in g[root]:
        pure(node,root)

pure(root,-1)
zones = dict()
def get_zones(node):
    if node in zones:
        return
    if not g[node]:
        zones[node]=1
        return
    ans = 1
    for br in g[node]:
        get_zones(br)
        ans += zones[br]
        if br%2==node%2:
            ans-=1
    zones[node]=ans

#zones = [get_zones(node) for node in g]
get_zones(root)
ans = sum(zones.values())
print(ans)
print(zones)
