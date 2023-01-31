n=int(input())
cnt=0
for i in range(9,-1,-1):
    for j in range(9,-1,-1):
        if j!=i:
            for k in range(9,-1,-1):
                if k!=i and k!=j:
                    for l in range(9,-1,-1):
                        if l!=i and l!=j and l!=k:
                            for m in range(9,-1,-1):
                                if m!=i and m!=j and m!=k and m!=l:
                                    cnt+=1
                                    if cnt==n:
                                        s=str(i)+str(j)+str(k)+str(l)+str(m)
                                        print(s)

