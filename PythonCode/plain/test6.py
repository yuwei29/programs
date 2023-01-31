import sys
a=sys.stdin.readlines()
a=''.join(a)

def dfs(s, depth):
    i=0
    leaf = 1
    while i<len(s):
        if i<len(s)-6 and s[i:i+3]=='for':
            leaf = 0
            stack=[]
            first = 1
            start = 0
            for j in range(i+3,len(s)):
                if s[j]=='{':
                    stack.append('{')
                    if first:
                        first = 0
                        start = j+1
                elif s[j]=='}':
                    stack.pop()
                    if not stack:
                        dfs(s[start:j],depth+1)
                        i=j+1
                        break
        else:
            i+=1
    if leaf:
        print(depth)

dfs(a,0)
                



