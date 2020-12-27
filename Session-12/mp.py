import multiprocessing
import time
import sys


def function():
	# print(__name__)
	for i in range(5):
		print("hey from child")
		time.sleep(1)

	sys.exit(3)



if __name__ == "__main__":
	process = multiprocessing.Process(target=function, daemon=True)


	print("Parent started")
	process.start()
	while process.exitcode == None:
		time.sleep(1)
	print(process.exitcode)
	print("Parent Ended")
