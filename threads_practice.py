import time
import threading


def calc_square(number):
    print("Calculate square numbers: ")
    for i in number:
        time.sleep(0.2)
        print("Square of " + str(i) + ": " + str(i*i))


def calc_cube(number):
    print("Calculate cube numbers: ")
    for i in number:
        time.sleep(0.2)
        print("")
        print("Cube of " + str(i) + ": " + str(i*i*i))


arr = [2, 3, 8, 9]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Successed")
