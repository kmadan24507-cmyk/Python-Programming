#1.MATHEMATICAL OPERATORS
#A.
num1 = 10
num2 = 20
print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division
print(num1 % num2)  # Modulus or Remainder
print(num1 ** num2) # Exponentiation or Power
print(num1 // num2) # Floor Division
#2.COMPARISON OPERATORS
#A.
num1 = 10
num2 = 20
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not equal to
print(num1 > num2)   # Greater than
print(num1 < num2)   # Less than
print(num1 >= num2)  # Greater than or equal to
print(num1 <= num2)  # Less than or equal to
#3.LOGICAL OPERATORS
#A. AND
num1 = 10
num2 = 20
print(num1 > 5 and num2 > 15)  # True and True -> True
print(num1 > 5 and num2 < 15)  # True and False -> False
print(num1 < 5 and num2 > 15)  # False and True -> False
print(num1 < 5 and num2 < 15)  # False and False -> False
#B.OR
num1 = 10
num2 = 20
print(num1 > 5 or num2 > 15)  # True or True -> True
print(num1 > 5 or num2 < 15)  # True or False -> True
print(num1 < 5 or num2 > 15)  # False or True -> True
print(num1 < 5 or num2 < 15)  # False or False -> False
#C.NOT
num1 = 10
print(not num1 > 5)  # not True -> False
print(not num1 < 5)  # not False -> True
#4. MEMBERSHIP OPERATORS
#A. IN
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False
#B. NOT IN
my_list = [1, 2, 3, 4, 5]
print(3 not in my_list)  # False
print(6 not in my_list)  # True
#5.IDENTITY OPERATORS
#A. IS
num1 = 10
num2 = 10
print(num1 is num2)  # True (both refer to the same object in memory)
#B. IS NOT
num1 = 10
num2 = 20
print(num1 is not num2)  # True (num1 and num2 refer to different objects in memory)
#6. BITWISE OPERATORS
#A. AND
num1 = 5  # In binary: 0101
num2 = 3  # In binary: 0011
print(num1 & num2)  # Bitwise AND: 0001 (1 in decimal)
#B. OR
num1 = 5  # In binary: 0101
num2 = 3  # In binary: 0011
print(num1 | num2)  # Bitwise OR: 0111 (7 in decimal)
#C. XOR
num1 = 5  # In binary: 0101
num2 = 3  # In binary: 0011
print(num1 ^ num2)  # Bitwise XOR: 0110 (6 in decimal)
#D. NOT
num1 = 5  # In binary: 0101
print(~num1)  # Bitwise NOT: 1010 (-6 in decimal)
#E. LEFT SHIFT
num1 = 5  # In binary: 0101
print(num1 << 1)  # Left shift by 1: 1010 (10 in decimal)
print(num1 << 2)  # Left shift by 2: 10100 (20 in decimal)
#F. RIGHT SHIFT
num1 = 5  # In binary: 0101
print(num1 >> 1)  # Right shift by 1: 0010 (2 in decimal)
print(num1 >> 2)  # Right shift by 2: 0001 (1 in decimal)
#7. ASSIGNMENT OPERATORS
num1 = 10
num1 += 5  # Equivalent to num1 = num1 + 5
print(num1)  # 15
num1 -= 3  # Equivalent to num1 = num1 - 3
print(num1)  # 12
num1 *= 2  # Equivalent to num1 = num1 * 2
print(num1)  # 24
num1 /= 4  # Equivalent to num1 = num1 / 4
print(num1)  # 6.0
num1 %= 5  # Equivalent to num1 = num1 % 5
print(num1)  # 1.0
num1 **= 3  # Equivalent to num1 = num1 ** 3
print(num1)  # 1.0
num1 //= 2  # Equivalent to num1 = num1 // 2
print(num1)  # 0.0
#8. TERNARY OPERATOR
num1 = 10
num2 = 20
result = "num1 is greater" if num1 > num2 else "num2 is greater"
print(result)  # Output: "num2 is greater"
