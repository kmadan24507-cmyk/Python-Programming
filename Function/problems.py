# PROBLEMS ON FUNCTIONS AND MODULES
# PART A ---> FUNCTION WITH ARGUMENTS ,  NO RETURN VALUE
# 1 ---> ADD TWO NUMBERS
def add(a,b):
    print(f"Sum = {a+b}")
add(10,20)
# 2 ---> SUBTRACT TWO NUMBERS
def sub(a,b):
    print(f"Sub = {a-b}")
sub(20,10)
# 3 ---> MULTIPLICATION
def mul(a,b):
    print(f"Mul = {a*b}")
mul(1,3)
# 4 ---> SQUARES
def squares(n):
    print(f"Squares of {n} = {n*n}")
squares(5)
# 5 ---> FIND MAXIMUM NUMBER
def maximum(a,b):
    if a > b:
        print(f"Maximum = {a}")
    else:
        print(f"Maximum = {b}")
maximum(1,2)
# 6 ---> FIND MINIMUM NUMBER
def minimum(a,b):
    if a < b:
        print(f"Minimum = {a}")
    else:
        print(f"Minimum = {b}")
minimum(1,2)
# 7 ---> EVEN AND ODD
def even_odd(n):
    if n % 2 == 0:
        print(f"Even = {n}")
    else:
        print(f"Odd = {n}")
even_odd(3)
even_odd(2)
# 8 ---> FIND PERCENTAGE
def percentage(scored,total):
    print(f"Percentage = {(scored / total)*100}")
percentage(540,600)
percentage(967,1000)
# 9 ---> LEAP YEAR
def leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(f"{year} = Leap year")
    else:
        print(f"{year} = Not A Leap year")
leap_year(2024)
# 10 ---> MULTIPLICATION TABLE
def mul_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
mul_table(5)
# 11 ---> ARMSTRONG NUMBER
def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(n))
        temp //= 10
    if sum == n:
        print("Armstrong Number")
    else:
        print("Not A Armstrong Number")
armstrong(153)
# 12 ---> PERFECT NUMBER
def perfect_number(n):
    temp = n
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum+=i
    if sum == n:
        print("Perfect Number")
    else:
        print("Not A Perfect Number")
perfect_number(6)
perfect_number(7)
# 13 ---> PALINDROME
def palindrome(n):
    rev = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    if rev == n:
        print("Palindrome Number")
    else:
        print("Not A Palindrome Number")
palindrome(121)
palindrome(123)
# 14 ---> REVERSE A NUMBER
def reverse(n):
    rev = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    print(f"Reverse of {n} = {rev}")
reverse(12345)
# 15 ---> SUM OF DIGITS
def sum_of_digits(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum+=digit
        temp //= 10
    print(f"Sum of {n} digits = {sum}")
sum_of_digits(1234)
# 16 ---> PRODUCT OF DIGITS
def pro_of_digits(n):
    prod = 1
    temp = n
    while temp > 0:
        digit = temp % 10
        prod*=digit
        temp //= 10
    print(f"Product Of Digits = {prod}")
pro_of_digits(123)
pro_of_digits(123456780)
# PART B ---> FUNCTIONS WITH RETURN VALUES
# 1 ---> SUM,SUB,MUL
def sum(a,b):
    return a + b
print(f"Sum = {sum(10,20)}")
def sub(a,b):
    return a - b
print(f"Sub = {sub(20,10)}")
def mul(a,b):
    return a * b
print(f"Mul = {mul(10,20)}")
# 2 ---> SQUARE AND CUBE
def square(n):
    return n * n
print(f"Square of 5 = {square(5)}")
def cube(n):
    return n * n * n
print(f"Cube of 5 = {cube(5)}")
# 3 ---> FACTORIAL
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
print(f"Factorial of 5 = {fact(5)}")
# 4 ---> FIBONACCI
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
    return a
print(f"Fibonacci of 10 = {fib(10)}")
# 5 ---> RETURN WHETHER NUMBER IS PRIME
def is_prime(n):
    if n < 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
print(is_prime(9))
print(is_prime(6))
# 6 ---> 