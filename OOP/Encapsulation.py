# ENCAPSULATION = Encapsulation means protecting data inside a class
# Ex : 
# A ---> WITHOUT ENCAPSULATION
class Bank:
    def __init__(self):
        self.balance = 100
    def show_balance(self):
        print(self.balance)
b = Bank()
b.balance = 1      # It Means It Loses Data
b.show_balance()
# B ---> WITH ENCAPSULATION
class Bank:
    def __init__(self):
        self._balance = 1000
    def show_balance(self):
        print(self._balance)
b1 = Bank()
b1.balance = 0
b1.show_balance()
# PROBLEMS
# 1 ---> 
class Student:
    def __init__(self,name):
        self.__name = name
    def display(self):
        print(f"Student Name = {self.__name}")
s = Student("Madan Kumar")
s.display()
# 2 --->
class Employee:
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
e = Employee(3000)
print(f"Salary = {e.get_salary()}")
# 3 ---> 
class Person:
    def __init__(self,age):
        self.__age = age
    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
p = Person(20)
print(p.get_age())
p.set_age(30)
print(p.get_age())
# 4 ---> 
class Student:
    def __init__(self):
        self.__marks = 0
    def set_method(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
    def get_method(self):
        return self.__marks
s = Student()
s.set_method(100)
print(f"Marks = {s.get_method()}")
# 5 ---> 
class Price:
    def __init__(self):
        self.__price = 0
    def set_price(self,price):
        if price >= 0:
            self.__price = price
        else:
            print("Invalid Price")
    def get_price(self):
        return self.__price
p = Price()
p.set_price(-90)
print(p.get_price())
# 6 ---> 
class Bank:
    def __init__(self):
        self.__balance = 0
    def deposit(self,amount):
        if amount >= 0:
            self.__balance+=amount
            print(f"{amount} has been deposited successfully")
        else:
            print("Invalid Amount")
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            self.__balance-=amount
            print(f"{amount} has been withdrawn successfully")
    def get_balance(self):
        return self.__balance
b = Bank()
b.deposit(1000)
print(b.get_balance())
b.withdraw(90)
print(b.get_balance())