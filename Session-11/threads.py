import threading
import time
import sys, os


# def func():
# 	print("Thread Started")
# 	start_time = time.time()
# 	while time.time() - start_time <= 10:
# 		print("Hey from thread")
# 		time.sleep(1)
# 	print("Thread Ended")

def func1():

    for i in range(5):
        print("Hello from func1")
        # os._exit(0)
        time.sleep(1)

def func2():

    for i in range(5):
        print("Hey from func2")
        time.sleep(1)


# print("Main thread started")
# start_time = time.time()

thread1 = threading.Thread(target=func1, daemon=True)
thread2 = threading.Thread(target=func2, daemon=True)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("All thread has completed")
# task to be done after all threads have completed their execution

# print("Main thread ended")