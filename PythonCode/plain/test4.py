def dfs(node):
    if node.leaf:
        print(node)
        return
    for branch in node.branches:
        dfs(branch)

def dfs1(node):
    if type(node[0])==type('str'):
        print(node[1])
        return
    dirs = 0
    for branch in node[0]:
        if type(branch)!=type('str'):
            dirs+=1
            br = (branch,node[1]+"/d"+str(dirs))
        else:
            br = (branch,node[1]+"/"+branch)
        dfs1(br)

def go():
    tree = [['f1',['f2','f3',['f4','f5']],'f6'],[['f7'],['f8','f9']],['f10','f11','f12'],[[['f13','f14']]]]
    tr = (tree,'root')
    dfs1(tr)

if __name__ == '__main__':
    go()