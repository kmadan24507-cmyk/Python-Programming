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
# 7 --->
class Student:
    def __init__(self):
        self.__marks = 0
    @property      # PROPERTY GETTER = Allows you to use methods like variables
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
          self.__marks = value
        else:
            print("Invalid Marks!")
s = Student()
s.marks = 90
print(f"Marks = {s.marks}")
# 8 --->
class Employee:
    def __init__(self):
        self.__salary = 0
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,amount):
        if amount >= 0:
            self.__salary =  amount
        else:
            print("Invalid Salary")
e = Employee()
e.salary = 100000
print(f"Employee Salary = {e.salary}")
# 9 ---> 
class Bank:
    def __init__(self):
        self.__balance = 0
    @property
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount >= 0:
            self.__balance+=amount
        else:
            print("Invalid Money")
    def withdraw(self,amount):
        if amount < 0:
            print("Invalid Amount")
        elif amount > self.__balance:
            print("Insufficient Money")
        else:
            self.__balance-=amount
b = Bank()
b.deposit(999)
print(b.balance)
b.withdraw(99)
print(b.balance)
# 10 ---> 
class BankAccount:
    def __init__(self,acc_num,holder_name,balance):
        self.__acc_num = acc_num
        self.__holder_name = holder_name
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"${amount} deposited successfully")
        else:
            print("Invalid Deposit Amount")
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Deposit Money")
        elif amount <= self.__balance:
            self.__balance-=amount
            print(f"${amount} withdrawn successfully")
        else:
            print("Insufficient Funds")
    def check_balance(self):
        print(f"{self.__holder_name}'s balance = ${self.__balance}")
    def transfer_money(self,other_account,amount):
        if amount <= 0:
            print("Invalid Transfer Amount")
        elif amount <= self.__balance:
            self.__balance-=amount
            other_account.__balance+=amount
            print(f"${amount} transfered successfully")
        else:
            print("Insufficient Balance")
b1 = BankAccount("1234","Madan Kumar",400)
b2 = BankAccount("4567","Dilip Kumar",900)
b1.check_balance()
b2.check_balance()
b1.deposit(100)
b2.deposit(100)
b1.check_balance()
b2.check_balance()
b1.withdraw(100)
b2.withdraw(100)
b1.check_balance()
b2.check_balance()
b1.transfer_money(b2,100)
b2.check_balance()