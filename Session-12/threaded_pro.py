n = 10
arr = []
import time

def odd(n):

	for i in range(n):
		if i % 2 != 0:
			arr.append(("ODD", i))
			time.sleep(0.5)


def even(n):

	for i in range(n):
		if i%2 == 0:
			arr.append(("EVEN", i))
			time.sleep(0.1)



import threading


thread = threading.Thread(target=odd, args=(n,))

thread.start()
even(n)

thread.join()

print(arr)