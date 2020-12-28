import threading
from queue import Queue
import random
import time

def printer(q):
	while True:
		val = q.get()
		if val == "quit":
			break
		print(val)


def generator(q):
	for i in range(20):
		# q.put(random.randint(0, 100))
		q.put(i)

	q.put("quit")


if __name__ == "__main__":
	q = Queue()
	printer_thread = threading.Thread(target=printer, args=(q,))
	generator_thread = threading.Thread(target=generator, args=(q,))

	printer_thread.start()
	time.sleep(2)

	generator_thread.start()

	printer_thread.join()
	generator_thread.join()
