import time
import sys

def factorial(n):
	if n == 0:
		return 1
	return factorial(n-1) * n


def lazy_printer():
	for i in range(10):
		print("Hey from child")
		time.sleep(1) 

	sys.exit(0)

n = int(input())

print(factorial(n))
# lazy_printer()