# arr = [int(i) for i in input().split(" ")]
# arr = list(map(int, input().split(" ")))

# print(*arr)
import multiprocessing
import time
import os

def function(x):
	print(x, "process_id:", os.getpid())
	time.sleep(3)
	return x+10


def multi_arg_function(x, y):
	print(x, ":", y, "process_id:", os.getpid())
	time.sleep(3)
	return x + y


if __name__ == "__main__":
	pool = multiprocessing.Pool(3)
	# arr = [1,2,3,4,5]
	# result = pool.map(function, arr)
	# print(result)
	# multi_arg_function(*(1,5)) #<- unpacking
	arr1 = [(1,5), (2, 4), (3, 3), (4,2), (5,1)]
	result = pool.starmap(multi_arg_function, arr1)
	print(result)


	# workers = []
	# for i in arr:
	# 	p = multiprocessing.Process(target=function, args=(i,))
	# 	p.start()
	# 	workers.append(p)

	# for worker in workers:
	# 	print(worker.join())

