import sys
import os
import time

python_file, input_file, correct_out_file = sys.argv[1], sys.argv[2], sys.argv[3]
output_file = "output.txt"


command = "python " + python_file + " < " + input_file + " > " + output_file


init_time = time.time()
ret = os.system(command)
final_time = time.time()

correct_output = open(correct_out_file).read()
output = open(output_file).read()


running_time = final_time - init_time
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