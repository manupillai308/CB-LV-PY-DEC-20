import os


ret_val = os.system("python python2.py")
# print("Manu")

if ret_val == -3:
	print("Error occured in python2.py")
else:
	print("Program exited successfully")