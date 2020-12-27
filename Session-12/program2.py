import subprocess
import time

cmd = "python program1.py"

print("Parent started")
# subprocess.run(cmd) # shell=True for UNIX
pipe = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
pipe.stdin.write(b"5")
pipe.stdin.close()
res = pipe.stdout.read()
# while pipe.returncode == None:
# 	print(pipe.returncode)
# 	time.sleep(1)
# time.sleep(3)

# pipe.kill()
# ret = pipe.communicate()
# print(ret)
print("Result of child:", res)
print("Parent Ended")
