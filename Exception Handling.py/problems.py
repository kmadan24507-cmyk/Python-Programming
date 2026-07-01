# 1 ---> ZERO DIVISION ERROR
try:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    print(f"Result = {a / b}")
except ZeroDivisionError:
    print("Cannot Divide By Zero")
# 2 ---> VALUE ERROR
try:
    n = int(input("Enter A Number : "))
    print(f"You Entered = {n}")
except ValueError:
    print("Please Enter A Valid Integer")
# 3 ---> TYPE ERROR
try:
    a = 10
    # b = "20" 
    b = 20
    print(a + b)
except TypeError:
    print("Cannot Add Different Data Types")
# 4 ---> NAME ERROR
try:
    name = "Madan"
    print(name)
except NameError:
    print("Variable Is Not Defined")
# 5 ---> INDEX ERROR
try:
    lst = [1,2,3]
    # print(lst[9])
    print(lst[0])
except IndexError:
    print("Index Is Out Of Range")
# 6 ---> KEY ERROR
try:
    d = {"A" : 10 , "B" : 20}
    # print(d["C"])
    print(d["A"])
except KeyError:
    print("Key Not Found")
# 7 ---> ATTRIBUTE ERROR
try:
    a = 10
    a.append(1)
except AttributeError:
    print("Attribute Does Not Exists")
# 8 ---> IMPORT ERROR
try:
    # from math import square
    from math import sqrt
except ImportError:
    print("Cannot Import The Requested Function")
# 9 ---> FILE NOT FOUND ERROR
try:
    with open("sample.txt","r") as f:
        data = f.read()
except FileNotFoundError:
    print("File Does Not Exists")
# 10 ---> MODULE NOT FOUND ERROR
try:
    # import abcxyz
    import abc
except ModuleNotFoundError:
    print("Module Not Found")
# 11 ---> TRY , EXCEPT , ELSE
try:
    a = 10
    # b = 0
    b = 8
    print(a/b)
except ZeroDivisionError:
    print("Division By Zero Is Not Allowed")
else:
    print("Division Completed")
# 12 ---> TRY , EXCEPT , FINALLY
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Division By Zero Is Not Allowed")
finally:
    print("Division Completed")
# 13 ---> 
try:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    print(a/b)
except IndexError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Zero Division By Zero Is Not Available")
# 14 ---> 
while True:
    try:
        n = int(input("Enter a number : "))
        print(f"You Entered = {n}")
        break
    except ValueError:
        print("Invalid Input . Try Again")
# 15 ---> CALCULATOR
try:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        print(a+b)
    elif choice == 2:
        print(a-b)
    elif choice == 3:
        print(a*b)
    elif choice == 4:
        print(a/b)
    else:
        print("Invalid Choice")
except ValueError:
    print("Please Enter Numbers Only")
except ZeroDivisionError:
    print("Cannot Divide By Zero")
# 16 ---> 
try:
    lst = [1,2,3,4]
    index = int(input("Enter Index : "))
    print(lst[index])
except IndexError:
    print("Index Out Of Range")
except ValueError:
    print("Please Enter A Valid Integer")