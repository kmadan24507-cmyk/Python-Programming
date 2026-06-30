# SLICING
#1.
name = "Madan Kumar"
print(name[0])
print(name[0:])
print(name[1:])
print(name[:3])
print(name[0:3])
print(name[0:7])
print(name[0:7:1])
print(name[0:5:2])
print(name[1:-1])
print(name[::3])
print(name[::-1])
#2. String Methods
text = "madanKumar"
print(text.capitalize())    # capitalize = First Letter Capital Rest of us are small
print(text.title())         # title = First Letter of Each Word Capital
print(text.swapcase())      # swapcase = Small Letter to Capital and Capital to Small
print(text.count("a"))      # count = Count the no.of "a" in text
print(text.casefold())      # casefold = Convert the string to lower case and remove all the special characters
print(text.center(25,"*"))  # center = Center the string and fill the remaining space with "*"
print(text.encode())        # encode = Convert the string to bytes
print(text.endswith("R"))   # endswith = Check if the string ends with "R" or not return boolean
print(text.expandtabs())    # expandtabs = Replace the tab character with spaces
print(text.find("a"))       # find = Return the index of first occurrence of "a"
text1 = "My name is {}".format("Ram")
print(text1)       
print(text.index("m"))      # index = Return the index of first occurrence of "m"
print(text.isalnum())       # isalnum = Check if all characters in the string are alphanumeric or not it return boolean
print(text.isalpha())       # isalpha = Check if all characters in the string are alphabetic or not it return boolean
print(text.isdigit())       # isdigit = Check if all characters in the string are digits or not it return boolean
print(text.isascii())       # isascii = Check if all characters in the string are ASCII characters or not it return boolean
print(text.isdecimal())     # isdecimal = Check if the string has any decimals
print(text.isidentifier())  # isidentifier = Check if the string is a valid identifier or not it return boolean
print(text.islower())       # islower = Check if all characters in the string are lowercase or not it return boolean
print(text.isupper())       # isupper = Check if all characters in the string are uppercase or not it returns boolean
text2 = "Hello World\n"
print(text2.isprintable())  # isprintable = Checks whether all characters in the string are printable.
print(text.isspace())       # isspace = Check if the string has a space
text3 = "-"
words = ["a", "b", "c"]
print(text3.join(words))
print(text.rfind("a"))     # rfind = Return the index of last occurrence of "a"
print(text.rindex("a"))    # rindex = Return the index of last occurrence of "a"

#3. String Formatting
name = "Madan Kumar"
age = 25
print("My name is {} and I am {} years old".format(name,age))
#4. f-strings
name = "Madan Kumar"
age = 25
print(f"My name is {name} and I am {age} years old")
#5. String Interpolation
name = "Madan Kumar"
age = 25
print("My name is %s and I am %d years old" % (name, age))
#6. String Concatenation
name = "Madan Kumar"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old")
#7. String Repetition
name = "Madan Kumar"
print(name * 3)
# 8. MATHS FUNCTIONS
import math
print(math.ceil(4.2))    # ceil = Return the smallest integer greater than or equal to 4.2
print(math.floor(4.2))   # floor = Return the largest integer less than or equal to 4.2
print(math.sqrt(16))    # sqrt = Return the square root of 16
print(math.pow(2, 3))   # pow = Return the value of 2 to the power of 3
print(math.pi)         # pi = Return the value of pi
print(math.e)          # e = Return the value of e
print(round(4.5678, 2)) # round = Return the value of 4.5678 rounded to 2 decimal places
print(abs(-4))         # abs = Return the absolute value of -4
print(math.comb(5,2))   # comb = Return the number of ways to choose 2 items from a set of 5 items without repetition and without order
print(math.perm(5,2))   # perm = Return the number of ways to choose 2 items from a set of 5 items without repetition and with order
print(math.factorial(5)) # factorial = Return the factorial of 5
print(math.gcd(48, 18)) # gcd = Return the greatest common divisor of 48 and 18
print(math.lcm(48, 18)) # lcm = Return the least common multiple of 48 and 18
print(math.fibonacci(10)) # fibonacci = Return the 10th number in the Fibonacci sequence
print(math.isprime(7)) # isprime = Return True if 7 is a prime number, otherwise return False
# PROBLEMS
# 1 . STRING LENGTH
# A ---> FOR LOOP
def string_len(s):
    count = 0
    for i in s:
        count+=1
    return count
s = input("Enter the string : ")
print(string_len(s))