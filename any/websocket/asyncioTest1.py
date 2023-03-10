import time
import asyncio

async def f(num,magic):
    print(f'from f {magic}',time.time())
    s=0
    for i in range(num):
        s+=i%magic
    print(f'from f {magic}',time.time())
    print(f'from f {magic}, sum = {s}')
    
async def test():
    num = int(1e9)
    task2 = asyncio.create_task(f(num,2))
    task3 = asyncio.create_task(f(num,3))
    print('in test func')
    # await task2
    # await task3
    print('finish?')

if __name__=='__main__':
    asyncio.run(test())