from threading import Thread
import time
def f(x,magic):
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

def test(num):
  threads=[]
  for i in range(2,7):
    t = Thread(target=f,args=(num,i))
    threads.append(t)
    t.start()

if __name__=='__main__':
  test(int(1e8))