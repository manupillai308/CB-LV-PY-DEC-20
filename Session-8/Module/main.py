# import factorial as utility
# import factorial
# from factorial import factorial
# from factorial import sum 

from factorial import *

# print(sum([1,2,3,4]))

# from factorial import sum as my_sum

# print(sum([1,2,3,4]))


n = int(input("Enter your number:"))

# # print("Factorial of your number is:", utility.factorial(n))
# # print("Sum of your number is:", utility.sum(n))

print("Factorial of your number is:", factorial(n))
print("Sum of your number is:", sum(n))