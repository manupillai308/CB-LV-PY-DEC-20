import threading
import os


queue = []


def printer():
	while True:
		if len(queue) > 0:
			i, data = queue.pop()
			print("\n\n\nFile name:", i)
			print(data, end="\n\n\n")		

		if len(queue) == 0 and all(all_readers_stopped):
			print("All threads exited. Reader stopped")
			return None


def reader(path, j):

	for i in os.listdir(path):
		file_path = os.path.join(path, i)
		f = open(file_path)
		data = f.read()
		queue.append((i, data))

	all_readers_stopped[j] = True
		# print("\n\n\nFile name:", i)
		# print(data, end="\n\n\n")



thread1 = threading.Thread(target=reader, args=("./Data/1",0))
thread2 = threading.Thread(target=reader, args=("./Data/2",1))
thread3 = threading.Thread(target=printer)

all_readers_stopped = [False] * 2
thread1.start()
thread2.start()
thread3.start()

