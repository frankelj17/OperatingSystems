# 2. 1. 2 process 1 parent process, 1 child process

import os

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumEven = 0
sumOdd = 0
n = os.fork()

if n > 0:
    for i in range(10):
        if a[i] % 2 == 0:
            sumEven = sumEven + a[i]
    par = os.getpid()
    print("Parent process " + str(par))
    print("Sum of even no. is " + str(sumEven))
else:
    for i in range(10):
        if a[i] % 2 != 0:
            sumOdd = sumOdd + a[i]
    chi = os.getpid()
    print("\nChild process " + str(chi))
    print("Sum of odd no. is " + str(sumOdd))
