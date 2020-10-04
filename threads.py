# 2. 2. 2 Threads

from os import name
import threading

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
           10, 11, 12, 13, 14]


def square_evens(num):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            print(threading.currentThread().
                  getName() + " Square of    "
                  + str(i) + ": " +
                  str(i * i))


def cube_odds(num):
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            print(str(threading.currentThread().
                      getName() + " Cube of      "
                      + str(i) + ": " +
                      str(i * i * i)))


thread1 = threading.Thread(target=square_evens,
                           name="Thread1",
                           args=(numbers,))
thread2 = threading.Thread(target=cube_odds,
                           name="Thread2",
                           args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
