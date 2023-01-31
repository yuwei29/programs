from collections import  Counter
from math import  comb
mod = int(1e9) + 7

s=''
import random 
slen = int(3e5)
alphas = 'abcdefghijklmnopqrstuvwxyz'
for i in range(slen):
    s+=random.choice(alphas)
print('start')

n = len(s)
cnt = Counter(s)
res = 0
for i in range(ord('a'),ord('z')+1):
    ch = chr(i)
    if (v:=cnt[ch]) < 2:
        continue
    res += comb(v,2) * (n-v)
    res %= mod
print(res)