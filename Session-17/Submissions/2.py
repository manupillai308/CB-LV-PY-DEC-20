import sys
import os
import subprocess
import time
# import resource
# import psutil <- install using pip: pip install psutil
import multiprocessing

# python_file, input_file, correct_out_file = sys.argv[1], sys.argv[2], sys.argv[3]
# output_file = "output.txt"
# timeout=5

# command = "python " + python_file + " < " + input_file + " > " + output_file

def run(python_file, input_file, correct_out_file, test_case_no):
	# ret = os.system(command)
	input_data = open(input_file).read()
	init_time = time.time()
	pipe = subprocess.Popen([sys.executable, python_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# pipe = subprocess.Popen("python " + python_file, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# pipe.stdin.write(input_data.encode("utf-8"))

	# output = open(output_file).read()

	# try:
	# 	pipe.wait(timeout=timeout)
	# except subprocess.TimeoutExpired:
	# 	pipe.kill()
	# 	print("Test case result-", "Time Limit Exceeded", end="")
	# 	running_time = time.time() - init_time
	# 	print("-", running_time,"s", sep="")
	# 	sys.exit(0)

	# mem_usage = 0
	# while pipe.poll() is None:
	# 	print(psutil.Process(pipe.pid).memory_full_info())
	# 	time.sleep(1)

	# output = pipe.stdout.read()
	# error = pipe.stderr.read()
	# final_time = time.time()

	# pipe.wait()
	try:
		output, error = pipe.communicate(input_data.encode("utf-8"), timeout=5)
	except subprocess.TimeoutExpired:
		pipe.kill()
		# subprocess._cleanup()
		# pipe.stdout.close()
		# pipe.stderr.close()
		return (test_case_no, "Timeout", time.time() - init_time)

	final_time = time.time()
	# print(resource.getrusage(resource.RUSAGE_CHILDREN))
	# sys.exit(0)

	if pipe.returncode != 0:
		# print("Error:\n", error.decode("utf-8"))
		# sys.exit(0)
		return (test_case_no, "Run Error", error.decode("utf-8"))

	output = output.decode("utf-8")
	output = output.replace("\r", "")

	running_time = final_time - init_time
	correct_output = open(correct_out_file).read()

	result = "Fail"
	if running_time < 1.0 and correct_output == output:
		result = "Pass"
	elif running_time > 1.0:
		result = "Time Limit Exceeded"

	# print("Test case result-", result, end=" ")
	# print("-", running_time,"s", sep="")
	return (test_case_no, result, running_time)


if __name__ == "__main__":

	test_case_dir = sys.argv[1]

	args = []
	for test_case_no in os.listdir(test_case_dir):
		root = os.path.join(test_case_dir, test_case_no)
		arg = ("./my_program.py", os.path.join(root, "input.txt"), os.path.join(root, "correct_output.txt"), test_case_no)
		args.append(arg)

	# print(args)
	p = multiprocessing.Pool(len(args))

	results = p.starmap(run, args)
	# print(results)
	import tabulate

	print(tabulate.tabulate(sorted(results), headers=["Test Case", "Result", "Time Taken/Error Description"],tablefmt="grid"))


# f = open(correct_out_file)
# correct_output = f.read()
#
#
# print(command)