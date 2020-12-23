# n = int(input("Enter the number:"))
import sys

def factorial(n):
	if n == 0:
		return 1

	return factorial(n-1) * n


# print(sys.argv, type(sys.argv))
n = int(sys.argv[1])
print("Factorial of your number", factorial(n))