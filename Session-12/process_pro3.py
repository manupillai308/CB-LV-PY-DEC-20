import multiprocessing
import os
import signal
import time
import sys



def function():
	print("Child Process ID:", os.getpid())
	print("Parent from Child Process ID:", os.getppid())



def handler(*args):
	print("Keyboard CTRL + C Pressed, am exiting")

	sys.exit(3)

if __name__ == "__main__":
	# process = multiprocessing.Process(target=function)
	# process.start()
	# print("Parent Process ID:", os.getpid())
	# print("Child Process ID:", process.pid)

	signal.signal(signal.SIGINT, handler)
	while True:
		time.sleep(1)

	# os.kill(os.getppid(), signal.SIGINT)
