a = [0.04621286, 0.80074771, 0.69927187, 0.08720757, 0.90229528,
       0.03143434, 0.46442943, 0.50341827, 0.63305951, 0.66882124]

# def f():   # UnboundLocalError: local variable 'a' referenced before assignment
#     a = a*2

# f()

# def f():
#     print(a)

# f() 
# works : [0.04621286, 0.80074771, 0.69927187, 0.08720757, 0.90229528, 0.03143434, 0.46442943, 0.50341827, 0.63305951, 0.66882124]
import random
class T:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self,x,y):
        self.x = x+y
        self.y = x-y

    def show(self):
        print(self.x,self.y)

t1 = T(2,3)

def f():
    x = int(10*random.random())
    y = int(10*random.random())
    t1.update(x,y)