# Tue Aug 15 20:22:34 2023hello0started
# Tue Aug 15 20:22:34 2023hello1started
# Tue Aug 15 20:22:34 2023hello2started
# Tue Aug 15 20:22:34 2023hello3started
# Tue Aug 15 20:22:34 2023hello4started
# Tue Aug 15 20:22:34 2023hello5started
# Tue Aug 15 20:22:34 2023hello6started
# Tue Aug 15 20:22:34 2023hello7started
# Tue Aug 15 20:22:34 2023hello8started
# Tue Aug 15 20:22:34 2023hello9started
# Tue Aug 15 20:22:38 2023hello0done
# Tue Aug 15 20:22:38 2023hello1done
# Tue Aug 15 20:22:38 2023hello2done
# Tue Aug 15 20:22:38 2023hello3done
# Tue Aug 15 20:22:38 2023hello4done
# Tue Aug 15 20:22:38 2023hello5done
# Tue Aug 15 20:22:38 2023hello6done
# Tue Aug 15 20:22:38 2023hello7done
# Tue Aug 15 20:22:38 2023hello8done
# Tue Aug 15 20:22:38 2023hello9done
# Time:4.01sec



import asyncio
import time

async def hello(i):
    print(f"{time.ctime()}hello{i}started")
    await asyncio.sleep(4)
    print(f"{time.ctime()}hello{i}done")

async def main():
    coros = [hello(i)for i in range(10)]
    await asyncio.gather(*coros)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())   
    end = time.time()
    print(f'Time:{end-start:.2f}sec')