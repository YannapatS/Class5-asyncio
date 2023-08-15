#Tue Aug 15 20:21:43 2023 hello 1 started
#Tue Aug 15 20:21:43 2023 hello 2 started
#Tue Aug 15 20:21:47 2023 hello 1 done
#Tue Aug 15 20:21:47 2023 hello 2 done
#Time: 4.01 sec

import asyncio
import time

async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
        task1 =asyncio.create_task(hello(1)) #returns immediately, the  task is creasted
        #await astncio.sleep(3)
        task2 =asyncio.create_task(hello(2))
        await task1
        await task2
if __name__ == '__main__':
      start = time.time()
      asyncio.run(main())
      end = time.time()
      print(f'Time: {end-start:.2f} sec')