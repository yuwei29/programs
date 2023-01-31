root=['f1','f2',['f3','f4'],'f5']
def bfs():
    for branch in root.branches:
        if branch.leaf:
            print(branch.name)
        else:
            pass

from collections import deque

def bfs1(node):
    visits=[]
    visits.append(node)
    q = deque()
    q.append(node)

    while q:
        s = q.popleft()
        print(s)
        if type(s)==type([]):
            for branch in s:
                if branch not in visits:
                    visits.append(branch)
                    q.append(branch)

bfs1(root)