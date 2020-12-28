import sys
import os
import subprocess
import time

python_file, input_file, correct_out_file = sys.argv[1], sys.argv[2], sys.argv[3]
# output_file = "output.txt"
timeout = 5

# command = "python " + python_file + " < " + input_file + " > " + output_file
command = "python " + python_file

# ret = os.system(command)
input_data = open(input_file).read()
init_time = time.time()
pipe = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# pipe.stdin.write(input_data.encode("utf-8"))

# output = open(output_file).read()
# output = pipe.stdout.read()
# error = pipe.stderr.read()

try:
	output, error = pipe.communicate(input_data.encode("utf-8"), timeout=timeout)
except subprocess.TimeoutExpired:
	pipe.kill()
	print("Test case result-", "Time Limit Exceeded", end="")
	print("-", time.time() - init_time,"s", sep="")
	sys.exit(0)

final_time = time.time()

if pipe.returncode != 0:
	print("Test case result-", "Run Error", end="")
	print("-", time.time() - init_time,"s", sep="")
	print(error.decode("utf-8"))
	sys.exit(0)

output = output.decode("utf-8")
output = output.replace("\r", "")

running_time = final_time - init_time
correct_output = open(correct_out_file).read()

result = "Fail"
if running_time < 1.0 and correct_output == output:
	result = "Pass"
elif running_time > 1.0:
	result = "Time Limit Exceeded"

print("Test case result-", result, end="")
print("-", running_time,"s", sep="")

# f = open(correct_out_file)
# correct_output = f.read()
#
#
# print(command)