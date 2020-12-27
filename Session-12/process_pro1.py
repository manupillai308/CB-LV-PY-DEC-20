import multiprocessing



def change_var(var, var1):

	var.append(10)
	var1.value = 20


if __name__ == "__main__":
	var = []
	var1 = multiprocessing.Value("i", 10)
	var3 = multiprocessing.Value("f", 0.21)
	
	print(var, var1.value)
	process = multiprocessing.Process(target=change_var, args=(var, var1))
	process.start()
	process.join()
	print(var, var1.value)