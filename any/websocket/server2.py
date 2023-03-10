import asyncio
import websockets

chatroom=['',0]
asyncio.new_event_loop()
async def hello(websocket):
  while 1:
    try:
       name = await websocket.recv()
    except:
       print('client left')
       return
    print(f">>> {name}")

    greeting = f"Hello {name}!"
    chatroom[0]=greeting
    chatroom[1]+=1
    print('msg cnt:',chatroom[1])
    await websocket.send(greeting)
    print(f"<<< {greeting}")

async def main():
    async with websockets.serve(hello, "192.168.43.162", 8763):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())