n = 10
arr = []
import time

def odd(n):

	for i in range(n):
		if i % 2 != 0:
			arr.append(("ODD", i))
			time.sleep(0.5)
	print("Child Array:", arr)


def even(n):

	for i in range(n):
		if i%2 == 0:
			arr.append(("EVEN", i))
			time.sleep(0.1)



import multiprocessing

if __name__ == "__main__":
	process = multiprocessing.Process(target=odd, args=(n,))

	process.start()
	even(n)

	process.join()

	print(arr)