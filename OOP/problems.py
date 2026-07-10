# A ----> Classes And Objects
# 1 --->
class Student:
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student()
s1.name = "K.Madan Kumar"
s1.age = 19
s2 = Student()
s2.name = "K.Dilip Kumar"
s2.age = 26
s1.display()
print()
s2.display()
# 2 --->
class Car:
    def display(self):
        print(f"Brand = {self.brand} , Model = {self.model}")
c = Car()
c.brand = "Toyota"
c.model = 'Corella'
c.display()
# 3 --->
class Book:
    def display(self):
        print(f"Title = {self.title} , Author = {self.author} , Price = {self.price}")
b1 = Book()
b1.title = "Python"
b1.author = "Madan"
b1.price = 789
b1.display()
b2 = Book()
b2.title = "Java"
b2.author = "Kuamr"
b2.price = 790
b2.display()
# 4 --->
class Employee:
    def display(self):
        print(f"Employee ID = {self.employee_id}")
        print(f"Name = {self.name}")
        print(f"Salary = {self.salary}")
    def annual_salary(self):
        print(f"Annual Salary = {self.salary * 12}")
e1 = Employee()
e1.employee_id = 1234
e1.name = "K.Madan Kumar"
e1.salary = 9
print("Employee 1 : ")
e1.annual_salary()
e1.display()
print()
# 5 --->
class Mobile:
    def display(self):
        print(f"Company = {self.company}")
        print(f"Model = {self.model}")
        print(f"Ram = {self.ram}")
        print(f"Storage = {self.storage}")
        print(f"Price = {self.price}")
    def discount(self,percentage):
        discount_amount = self.price * percentage / 100
        final_price = self.price - discount_amount
        print(f"Original = ${self.price}")
        print(f"Discount = {percentage}")
        print(f"Final Price = ${final_price}")
m1 = Mobile()
m1.company = "Samsung"
m1.model = "S24"
m1.ram = "8 GB"
m1.storage = "256 GB"
m1.price = 750000
m1.display()
m1.discount(10)
# Problem 6 - Circle
class Circle:
    def display(self):
        print(f"Radius : {self.radius}")
    def area(self):
        area = 3.14 * self.radius ** 2
        print(f"Area : {area}")
    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        print(f"Circumference : {circumference}")
# Object 1
c1 = Circle()
c1.radius = 7
circles = [c1]
for circle in circles:
    circle.display()
    circle.area()
    circle.circumference()
    print()
# 7 --->
class Laptop:
    def display(self):
        print(f"Brand     : {self.brand}")
        print(f"Processor : {self.processor}")
        print(f"RAM       : {self.ram}")
        print(f"Storage   : {self.storage}")
        print(f"Price     : ₹{self.price}")
    def upgrade_ram(self,new_ram):
        self.ram = new_ram
        print(f"RAM upgraded = {self.ram}")
    def disount(self,percent):
        discount_amount = self.price * percent / 100
        final_price = self.price - discount_amount
        print(f"Original Price : ₹{self.price}")
        print(f"Discount       : {percent}%")
        print(f"Final Price    : ₹{final_price:.2f}")
# Laptop 1
l1 = Laptop()
l1.brand = "Dell"
l1.processor = "Intel i5"
l1.ram = "8 GB"
l1.storage = "512 GB SSD"
l1.price = 65000
laptops = [l1]
for laptop in laptops:
    laptop.display()
    print()
print("Upgrading RAM of Laptop 1...")
l1.upgrade_ram("16 GB")
l1.display()
# 8 --->
class Movie:
    def display(self):
        print(f"Title = {self.title}")
        print(f"Hero = {self.hero}")
        print(f"Director = {self.director}")
        print(f"Rating = {self.rating}")
        print(f"Ticket Price = {self.ticket_price}")
    def is_hit(self):
        if self.rating >= 8:
            print("Hit Movie")
        else:
            print("Average Movie")
    def book_ticket(self,quantity):
        total = self.ticket_price * quantity
        print(f"Tickets Booked = {quantity}")
        print(f"Total Amount = {total}")
m1 = Movie()
m1.title = "Pushpa 2"
m1.hero = "Allu Arjun"
m1.director = "Sukumar"
m1.rating = 8.9
m1.ticket_price = 300
m2 = Movie()
m2.title = "Kalki 2898 AD"
m2.hero = "Prabhas"
m2.director = "Nag Ashwin"
m2.rating = 9.2
m2.ticket_price = 350
m3 = Movie()
m3.title = "Devara"
m3.hero = "Jr.NTR"
m3.director = "Koratala Shiva"
m3.rating = 7.5
m3.ticket_price = 250
movies = [m1,m2,m3]
for i in movies:
    i.display()
    i.is_hit()
    i.book_ticket(5)
# 9 --->
class BankAccount:
    def display(self):
        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.balance}")
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance")
    def check_balance(self):
        print(f"Current Balance : ₹{self.balance}")
a1 = BankAccount()
a1.account_number = 1001
a1.holder_name = "Madan Kumar"
a1.balance = 50000
accounts = [a1]
for account in accounts:
    account.display()
    account.check_balance()
    print()
print("----- Transactions -----")
a1.deposit(10000)
a1.withdraw(15000)
a1.check_balance()
# 10 --->
class Animal:
    def display(self):
        print(f"Name = {self.name}")
        print(f"Species = {self.species}")
        print(f"Age = {self.age}")
        print(f"Sound = {self.sound}")
    def make_sound(self):
        print(f"{self.name} says {self.sound}")
    def birthday(self):
        self.age+=1
        print(f"Happy birthday {self.name}")
        print(f"New Age = {self.age} years")
a = Animal()
a.name = "Chintu"
a.species = "Dog"
a.age = 5
a.sound = "Barks"
a.display()
a.make_sound()
a.birthday()
