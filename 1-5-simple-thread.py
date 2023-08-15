#Time: 0.00
#Task B: Computer 1+2
#Task A: Computer 1+2
#Time: 1.01
#Time: 1.01
#Task B: Computer 3+3
#Task A:Sum = 3
#Time: 2.01
#Task B:Sum = 6
#Time: 3.02 sec


import asyncio
import time 
from concurrent.futures.thread import ThreadPoolExecutor

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0 
    for number in numbers:
        print(f'Task {name}: Computer {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    print(f'Task {name}:Sum = {total}\n')

start =time.time()

loop = asyncio.get_event_loop()
task = [
        loop.create_task(sum("A", [1,2])),
        loop.create_task(sum("B", [1,2,3])),
]
loop.run_until_complete(asyncio.wait(task))
loop.close

end= time.time()
print(f'Time: {end-start:.2f} sec')