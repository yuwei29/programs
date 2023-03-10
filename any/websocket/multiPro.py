import time
from multiprocessing import Pool
def f(x):
  x,magic = x
  print(f'x={x},magic={magic}')
  sum=0
  scale=0
  unit=int(1e7)
  t1=time.time()
  for i in range(x):
    sum+=i%magic
    if sum//unit>scale:
      scale=sum//unit
      print(f'from f {magic}:',scale)
  t2=time.time()
  print(f'from f {magic}, t2-t1=',t2-t1)
  print(f'from f {magic}, sum=',sum)
  

if __name__ == '__main__':
    num = int(1e8)
    gt1=time.time()
    with Pool(5) as p:
        p.map(f,[(num,2),(num,3),(num,4),(num,5),(num,6)])
    gt2=time.time()
    print(f'gt2-gt1={gt2-gt1}')