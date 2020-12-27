import sys
import os
import subprocess
import time

python_file, input_file, correct_out_file = sys.argv[1], sys.argv[2], sys.argv[3]
output_file = "output.txt"


# command = "python " + python_file + " < " + input_file + " > " + output_file
command = "python " + python_file


init_time = time.time()
# ret = os.system(command)
input_data = open("input.txt").read()
pipe = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
final_time = time.time()
pipe.stdin.write(input_data.encode("utf-8"))

# output = open(output_file).read()
output = pipe.stdout.read()
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