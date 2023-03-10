import time
from concurrent.futures import ProcessPoolExecutor
 
# function to execute in a new process
def f(num,magic):
    print(f'from f {magic}',time.time())
    s=0
    for i in range(num):
        s+=i%magic
    print(f'from f {magic}',time.time())
    print(f'from f {magic}, sum = {s}')
 
# entry point
def test():
    # create the process pool executor
    num=int(1e8)
    with ProcessPoolExecutor(5) as exe:
        # issue the task asynchronously
        future2 = exe.submit(f,num,2)
        future3 = exe.submit(f,num,3)
        # do other things, like report a message
        print('Main is doing other things...')
        # wait for the task to complete
        # _ = future.result()

if __name__ == '__main__':
    test()