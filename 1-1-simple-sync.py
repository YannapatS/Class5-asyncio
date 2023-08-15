# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3
# Task B: Computing 0+1
# Time: 2.01
# Task B: Computing 1+2
# Time: 3.01
# Task B: Computing 3+3
# Time: 4.02
# Task B: Sum = 6
# Time: 5.02 sec

import time 

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

#
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    #
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#
task = [
    sum("A", [1, 2]),
    sum("B", [1,2,3]),
]
end = time.time()
print(f'Time: {end-start:.2f} sec')
