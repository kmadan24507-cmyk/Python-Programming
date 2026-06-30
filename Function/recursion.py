# RECURSION = Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller versions of the same problem.
# PROBLEMS
# 1 . SUM OF A LIST
def sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum(lst[1:])
lst = list(map(int,input("Enter The Numbers In The List : ").split()))
print(f"The Sum Of Numbers In The List = {sum(lst)}")
# 2 . PRODUCT OF A LIST
def product(lst):
    if not lst:
        return 1
    else:
        return lst[0] * product(lst[1:])
lst = list(map(int,input('Enter The Numbers In The List : ').split()))
print(f"The Product Of Numbers In The list = {product(lst)}")
# 3 . FACTORIAL
def fact(n):
    if n == 0 and n == 1:
        return 1
    else:
        return n * fact(n-1)
n = int(input("Enter The Number : "))
print(f"The Factorial of {n} is {fact(n)}")
# 4 . FIBONACCI
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the n : "))
print(f"The Fibonacci series of {n} = {fibonacci(n)}")
# 4 . SUM OF A DIGITS IN A NUMBER
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n//10)
print(f"The Sum Of Digits In A Number = {sum_of_digits(123)}")
# 5 . EXPONENTATION --> (2,3) = 2 POWER 3
def exponentation(a,b):
    if b == 0:
        return 1
    else:
        return a * exponentation(a,b-1)
print(f"Exponentation of (2,3) = {exponentation(2,3)}")
