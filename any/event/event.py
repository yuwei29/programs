from threading import Thread

g = 0
tmp = 0
def check():
    global tmp
    while 1:
        if g-tmp>5:
            print(g,tmp)
            tmp=g

def f():
    global g
    while 1:
        g+=1
def h():
    global g
    while 1:
        if g%2==0:
            g+=3
    
def test():
    ts = [None]*3
    ts[0]=Thread(target=f,args=())
    ts[1]=Thread(target=h,args=())
    ts[2]=Thread(target=check,args=())
    for i in range(3):
        ts[i].start()

test()