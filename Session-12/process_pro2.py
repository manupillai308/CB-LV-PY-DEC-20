import multiprocessing
import time
import signal
import os
import sys

def handler_function(*args):

	print("I'm unresponsive, hence exiting.")
	sys.exit(5)


def infinite():

	print("Child Start")
	signal.signal(signal.SIGINT, handler_function)
	while True:

		time.sleep(1)

	print("Child End")




if __name__ == "__main__":
	print("Parent Start")
	process = multiprocessing.Process(target=infinite)
	process.start()
	start_time = time.time()
	unresponsive = True

	while time.time() - start_time <= 5:
		if not process.is_alive():
			unresponsive = False
			break

	if unresponsive:
		print("Process unresponsive")
		os.kill(process.pid, signal.SIGINT) #2
		print("Process Killed")

	process.join()
	print("Exitcode:", process.exitcode)
	print("Parent End")