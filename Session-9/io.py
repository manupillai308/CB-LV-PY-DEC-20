import sys



# print(type(sys.stdin), type(sys.stdout))

f = open("./Session-9/my_file.txt")
sys.stdin = f
out = open("./Session-9/output_file.txt", "w")
sys.stdout = out

a = int(input())
b = int(input())
c = int(input())


# print(a+b+c, file=out)

print(a+b+c)