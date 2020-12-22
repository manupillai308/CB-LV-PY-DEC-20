import sys


input_file_path = input("Enter input file:")
output_file_path = input("Enter output file:")
# python_file_path = input("Enter python file:")


sys.stdin = open(input_file_path)
sys.stdout = open(output_file_path, "w")

### your code
# n
# n space separated integers

n = int(input())
arr = [int(i) for i in input().split(" ")]

arr.sort()
print(*arr)










