import multiprocessing
# from queue import Queue
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
	q = multiprocessing.Queue()
	lock = multiprocessing.Lock()
	printer_pro = multiprocessing.Process(target=printer, args=(q,))
	generator_pro = multiprocessing.Process(target=generator, args=(q,))

	printer_pro.start()
	time.sleep(2)

	generator_pro.start()

	printer_pro.join()
	generator_pro.join()
