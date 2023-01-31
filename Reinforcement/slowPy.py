import time
n = int(1e9)
sum = 0
t1 = time.time()
for i in range(n):
    sum+=i%2
t2 = time.time()
print(t2-t1)
print(sum)