# # print("Hello world")
# n = int(input())
# import random


# print("Number entered is:", n)


# print(*[random.randint(1, 1000000) for i in range(10000)])

arr = [int(i) for i in input().split(" ")]
arr.sort()
print(*arr)