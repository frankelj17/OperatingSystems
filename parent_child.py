# 2. 1. 2 process 1 parent process,
# 1 child process

import os

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
           10, 11, 12, 13, 14]


procPID = os.fork()

if procPID > 0:
    parentPROC = os.getpid()
    print("Parent Process: " + str(parentPROC))
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            print("Square of    " + str(i) +
                  ": " + str(i * i))

else:
    childPROC = os.getpid()
    print("\nChild Process: " + str(childPROC))
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            print("Cube of      " + str(i) +
                  ": " + str(i * i * i))
