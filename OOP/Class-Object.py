# OOP(Objected Oriented Programming) 
# OOP ---> Is A Way Of Writing Programs By Creating Objects That Represents Real-World Things
# In OOP ---> Properties  = Attributes(Variables) , Actions = Methods(Functions)
# Ex : 
class student:
    name = "Madan"
    age = 20
s1 = student()
print(s1.name)
print(s1.age)
# METHODS = A Function inside a class
# Ex : 
class Student:
    name = "K.Madan Kumar"
    age = 19
    def details(self):
        print(f"Name = {self.name} , Age = {self.age}")
s1 = Student()
s1.details()
# CONSTRUCTOR = A Special Method That Is Automatically Called When An Object Is Created
# Ex : 
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = Student("Madan",19)
print(s1.name)
print(s1.age)
# PROBLEMS
# 1 ---> 
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
student1 = Student("Madan",19)
print(student1.name)
print(student1.age)
# 2 ---> 
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
student1 = Student("Madan",19)
student2 = Student("Dilip",26)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
# 3 ---> 
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
car1 = Car("Toyota","Supra",2019)
car2 = Car("Honda","City",2024)
print(car1.brand)
print(car1.model)
print(car1.year)
print(car2.brand)
print(car2.model)
print(car2.year)
# 4 ---> 
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
book = Book("Python","John Smith",500)
print(book.title)
print(book.author)
print(book.price)
# 5 ---> 
class Mobile:
    def __init__(self,company,model,storage):
        self.company = company
        self.model = model
        self.storage = storage
    def display(self):
        print(f"Company = {self.company}")
        print(f"Model = {self.model}")
        print(f"Storage = {self.storage}")
mobile = Mobile("IQOO","IQ 13","256 GB")
print(mobile.company)
print(mobile.model)
print(mobile.storage)
# 6 ---> 
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length+self.breadth)
rect = Rectangle(10,10)
print(f"Area Of Rectangle = {rect.area()}")
print(f"Perimeter Of Rectangle = {rect.perimeter()}")
# 7 ---> 
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
circle = Circle(7)
print(f"Area Of Circle = {circle.area()}")
# 8 ---> 
class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
square = Square(5)
print(f"Area = {square.area()}")
print(f"Perimeter = {square.perimeter()}")
# 9 ---> 
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} Says Woof")
dog1 = Dog("Chimtu","Kukka Jathi")
print(dog1.name)
print(dog1.breed)
print(dog1.bark())
# 10 ---> 
class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def meow(self):
        print(f"{self.name} says Meow")
cat1 = Cat("Pilli","Yellow")
print(cat1.name)
print(cat1.color)
cat1.meow()
# 11 ---> 
class Temparature:
    def __init__(self,celsius):
        self.celsius = celsius
    def fahrenheit(self):
        return (self.celsius*9/5)+32
temp = Temparature(45)
print(f"Celsius = {temp.celsius}")
print(f"Fahrenheit = {temp.fahrenheit()}")
# 12 ---> 
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def describe(self):
        print(f"{self.name} is {self.age} years old")
    def birthday(self):
        self.age+=1
        print("Happy Birthday")
animal = Animal("Cat",4)
animal.describe()
animal.birthday()
animal.describe()
# 13 ---> 
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} has been deposited")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
        else:
            print("Insufficient Money")
    def display(self):
        print(f"Owner = {self.owner}")
        print(f"Balance = {self.balance}")
account = Account("Madan",1000)
account.display()
account.deposit(1000)
account.display()
account.withdraw(1000)
account.display()
# 14 --->
class Library:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True
    def borrow(self):
        if self.available:
            self.available = False
            print("Book Borrowed Successfully")
        else:
            print("Book Is Already Borrowed")
    def return_book(self):
        self.available = True
        print("Book Returned Successfully")
    def display(self):
        print(f"Title = {self.title}")
        print(f"Author = {self.author}")
        print(f"Available = {self.available}")
book = Library("Python","John")
book.display()
book.borrow()
book.display()
book.borrow()
book.return_book()
book.display()
# 15 ---> 
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name = {self.name}")
        print(f"Marks = {self.marks}")
    def is_pass(self):
        if self.marks >= 35:
            print("Result = Pass")
        else:
            print("Result = Fail")
student1 = Student("Madan",32)
student2 = Student("Kumar",99)
student1.display()
student1.is_pass()
student2.display()
student2.is_pass()
# 16 ---> 
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def increment(self):
        self.salary*=10
    def display(self):
        print(f"Name = {self.name}")
        print(f"Salary = {round(self.salary,2)}")
emp = Employee("Madan",200)
emp.display()
emp.increment()
emp.display()
# 17 ---> 
class ATM:
    def __init__(self,pin,balance):
        self.pin = pin
        self.balance = balance
    def check_balance(self,entered_pin):
        if entered_pin == self.pin:
            print(f"Balance = {self.balance}")
        else:
            print("Invalid PIN")
    def withdraw(self,entered_pin,amount):
        if entered_pin != self.pin:
            print("Invalid PIN")
        elif amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance-=amount
            print("Please Collect your cash")
    def deposit(self,entered_pin,amount):
        if entered_pin == self.pin:
            self.balance+=amount
        else:
            print("Invalid PIN")
atm = ATM(123,1000)
atm.check_balance(123)
atm.deposit(123,500)
atm.check_balance(123)
atm.withdraw(123,500)
atm.check_balance(123)
# 18 ---> 
class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count+=1
s1 = Student("Madan")
s2 = Student("Kumar")
s3 = Student("Dilip")
print(f"Total tudents = {Student.count}")
# 19 ---> 
class Employee:
    company = "GOOGLE"
    def __init__(self,name):
        self.name = name
print(Employee.company)
Employee.company = "Apple"
print(Employee.company)
e = Employee("Madan")
print(e.company)
# 20 ---> STATIC METHOD
class Calculator:
    @staticmethod
    def add(a,b):
        return a + b
print(Calculator.add(1,2))
# 21 ---> 
class Rectangle:
    @staticmethod
    def area(length,width):
        return length * width
print(Rectangle.area(1,2))
# 22 ---> 
class Even_number:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
print(Even_number.is_even(3))
print(Even_number.is_even(6))
# 23 --->
class Calculator:
    @staticmethod
    def maximum(a,b):
        if a > b:
            return a
        else:
            return b
print(Calculator.maximum(8,9))
# 24 ---> 
class University:
    total_departments = 0
    def __init__(self,department_name):
        self.department_name = department_name
        University.total_departments+=1
    def display(self):
        print(f"Department = {self.department_name}")
    @classmethod
    def show_department(cls):
        print(f"Total Departments = {cls.total_departments}")
    @staticmethod
    def is_weekend(day):
        if day.lower() in ["Saturday" , "Sunday"]:
            return True
        else:
            return False
    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"
d1 = University("Computer Science")
d2 = University("Electronics")
d3 = University("Mechanical")
d4 = University("Civil")

# Display Departments
d1.display()
d2.display()
d3.display()
d4.display()

print()

# Class Method
University.show_department()

print()

# Static Method - Weekend
print("Is Saturday Weekend?", University.is_weekend("Saturday"))
print("Is Monday Weekend?", University.is_weekend("Monday"))

print()

# Static Method - Grade
print("Grade for 95:", University.grade(95))
print("Grade for 82:", University.grade(82))
print("Grade for 65:", University.grade(65))
print("Grade for 40:", University.grade(40))