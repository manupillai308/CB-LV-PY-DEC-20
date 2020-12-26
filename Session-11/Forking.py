import os
import time

var = 10

def func1():

    for i in range(100):
        print("Hello from func1")
        time.sleep(1)

def func2():

    for i in range(100):
        print("Hey from func2")
        time.sleep(1)



ret = os.fork() #only works in Unix based OS

if ret != 0:
    print("Starting in Parent")
    var = 20
    func1()
    print("Parent End")

else:
    print("Starting in Child")
    var = 30
    func2()
    print("Child End")


print(var)