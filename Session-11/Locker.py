import threading
import os
import time

# Custom Made Lock Object
# lock = False

# def reader(path):

# 	for i in os.listdir(path):
# 		file_path = os.path.join(path, i)
# 		f = open(file_path)
# 		data = f.read()
# 		while lock:
# 			time.sleep(0.01)
# 		if not lock:
# 			lock = True
# 			print("\n\n\nFile name:", i)
# 			print(data, end="\n\n\n")
# 			lock = False


lock = threading.Lock()

def reader(path):

	for i in os.listdir(path):
		file_path = os.path.join(path, i)
		f = open(file_path)
		data = f.read()
		lock.acquire(blocking=True)
		print("\n\n\nFile name:", i)
		print(data, end="\n\n\n")
		lock.release()


# thread1 = threading.Thread(target=reader, args=("./Data/1",))
thread1 = threading.Timer(3, reader, args=("./Data/1",))
thread2 = threading.Thread(target=reader, args=("./Data/2",))

thread1.start()
thread2.start()

