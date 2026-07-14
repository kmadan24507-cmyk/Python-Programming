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
# 11 --->
class Rectangle:
    def display(self,length,width):
        self.length = length
        self.width  = width
        print(f"Length = {self.length}")
        print(f"Width = {self.width}")
    def area(self):
        print(f"Area = {self.length} * {self.width}")
    def perimeter(self):
        print(f"Perimeter = {2 * (self.length + self.width)}")
    def is_square(self):
        if self.length == self.width:
            print("This Is A square")
        else:
            print("This Is A Rectangle")
r = Rectangle()
r.display(10,20)
# r.display(10,10)
r.area()
r.perimeter()
r.is_square()
# 12 --->
class Student:
    def display(self):
        print(f"Name = {self.name}")
        print(f"Marks - 1 = {self.mark_1}")
        print(f"Marks - 2 = {self.mark_2}")
        print(f"Marks - 3 = {self.mark_3}")
    def total(self):
        return self.mark_1 + self.mark_2 + self.mark_3
    def average(self):
        return round(self.total() / 3,2)
    def result(self):
        if self.average() >= 35:
            print("Pass")
        else:
            print("Fail")
s = Student()
s.name = "K.Madan Kumar"
s.mark_1 = 90
s.mark_2 = 91
s.mark_3 = 93
s.display()
print(f"Total Marks = {s.total()}")
print(f"Average = {s.average()}")
s.result()
# 13 --->
class Product:
    def display(self):
        print(f"Product Name = {self.name}")
        print(f"Price = {self.price}")
        print(f"Quantity = {self.quantity}")
    def total_cost(self):
        print(f"Total Cost = {self.price * self.quantity}")
    def discount(self,percent):
        discount_amount = self.total_cost() * percent / 100
        final_amount = self.total_cost - discount_amount
        print(f"Final Amount ={final_amount}")
p = Product()
p.name = "Laptop"
p.price = 5000000
p.quantity = 4
p.display()
p.total_cost()
p.discount(10)
# 13 --->
class Product:
    def display(self):
        print(f"Product Name = {self.name}")
        print(f"Price = {self.price}")
        print(f"Quantity = {self.quantity}")
    def total_cost(self):
        return self.price * self.quantity
    def discount(self,percent):
        total = self.total_cost()
        discount_amount = total * percent / 100
        final_amount = total - discount_amount
        print(f"Final Amount ={final_amount}")
    def stock_status(self):
      if self.quantity >= 10:
        print("In Stock")
      else:
        print("Low Stock")
p = Product()
p.name = "Laptop"
p.price = 5000000
p.quantity = 4
p.display()
p.total_cost()
p.discount(10)
p.stock_status()
# 14 --->
class LibraryBook:
    def display(self):
        print(f"Title = {self.title}")
        print(f"Author = {self.author}")
        print(f"Price = {self.price}")
        if self.is_issued:
            print(f"Staus = Issued")
        else:
            print(f"Status = Available")
    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book Issued Successfully")
        else:
            print("Book Already Issued")
    def return_book(self):
        if self.is_issued:
            is_issued = False
            print("Book Returned Successfully")
        else:
            print("Book Was Not Issued")
    def change_price(self,new_price):
        self.price = new_price
        print("Price Updated Successfully")
l = LibraryBook()
l.title = "Python Programming"
l.author = "K.Madan Kumar"
l.price = 890
l.is_issued = False
l.display()
l.issue_book()
l.display()
l.issue_book()
l.return_book()
l.display()
l.change_price(900)
l.display()
# B ---> Constructors (__init__)
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
s = Student("Madan",19)
s.display()
# 1 --->
class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print(f"Brand  : {self.brand}")
        print(f"Model  : {self.model}")
        print(f"Price  : ${self.price}")
    def discount(self,percent):
        discount_ = self.price * percent / 100
        final_price = self.price - discount_
        print(f"Original Price   : {self.price}")
        print(f"Discount         : {percent}")
        print(f"Final Price      : {final_price}")
c = Car("Toyota","Corolla",1500000)
c.display()
c.discount(10)
# 2 --->
class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def display(self):
        print(f"Account Number   :   {self.account_number}")
        print(f"Holder Name      :   {self.holder_name}")
        print(f"Balance          :   {self.balance}")
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"${amount} Deposited Successfully")
            print(f"Current Balance  : ${self.balance}")
        else:
            print("Amount Must Be Positive")
    def withdraw(self,amount):
        if amount > 0:
            self.balance-=amount
            print(f"${amount} Withdawn Successfully")
            print(f"Current Balance : {self.balance}")
        elif amount > self.balance:
            print("Insufficient Funds")
        else:
            print("Amount Must be Positive")
    def transfer(self,reciever,amount):
        if amount > self.balance:
            print("Transfer Failed - Insufficient Balance")
        elif amount < 0 :
            print("Amount Must Be Positive")
        else:
            self.balance-=amount
            reciever.balance+=amount
            print(f"{amount} Transfered Successfully")
            print(f"Current Balance = {self.balance}")
b1 = BankAccount(1001,"K.Madan Kumar",200)
b2 = BankAccount(1002,"K.Dilip Kumar",200)
b1.display()
b2.display()
b1.withdraw(100)
b1.transfer(b2,100)
b1.display()
b2.display()
# 3 --->
class ShoppingCart:
    def __init__(self,product_name,price,quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    def display(self):
        print(f"Product Name   : {self.product_name}")
        print(f"Price          : {self.price}")
        print(f"Quantity       : {self.quantity}")
    def total_bill(self):
        return self.price * self.quantity
    def discount(self,percent):
        total = self.total_bill()
        discount_amount = total * percent / 100
        final_bill = total - discount_amount
        print(f"Discount   :  {percent}")
        print(f"Final Bill :  {final_bill}")
        return final_bill
    def gst(self,percent):
        final_bill = self.discount(10)
        gst_amount = final_bill * 18/100
        amount_after_gst = final_bill + gst_amount
        print(f"GST  : {gst_amount}")
        print(f"Amount After GST : {amount_after_gst}")
    def change_quantity(self,new_quantity):
        self.quantity = new_quantity
        print("Quantity Updated Successfully")
c = ShoppingCart("laptop",200,2)
c.display()
c.total_bill()
c.discount(10)
c.gst(10)
c.change_quantity(4)
c.display()
c.total_bill()
# 4 --->
class ATM:
    def __init__(self,account_holder,pin,balance):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
    def display(self):
        print(f"Account Holder Name  : {self.account_holder}")
        print(f"Balance              : {self.balance}")
    def check_pin(self,entered_pin):
        if self.pin == entered_pin:
            print("PIN Verified")
        else:
            print("Invalid PIN")
    def deposit(self,entered_pin,amount):
        if self.pin == entered_pin:
            if amount <= 0:
                print("Transaction Failed")
            else:
                self.balance+=amount
                print(f"{amount} Deposited Successfully")
        else:
            print("Invalid PIN")
    def withdraw(self,entered_pin,amount):
        if self.pin == entered_pin:
           if amount <= 0:
            print("Amount Must be Positive")
           elif amount > self.balance:
            print("Amount Must not Exceed Balance")
           else:
               self.balance-=amount
               print(f"{amount} Withdrawn Successfully")
    def change_pin(self,old_pin,new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            print("PIN Changed Successfully")
        else:
            print("Incorrect Old PIN")
a = ATM("K.Madan Kumar",1234,100)
a.display()
a.deposit(1234,100)
a.withdraw(1234,10)
a.change_pin(1234,5678)
a.withdraw(5678,10)
a.display()
# 5 --->
class Library:
    def __init__(self,book_name,author,price,available_copies):
        self.book_name = book_name
        self.author = author
        self.price = price
        self.available_copies = available_copies
    def display(self):
        print(f"Book Name        : {self.book_name}")
        print(f"Author           : {self.author}")
        print(f"Price            : {self.price}")
        print(f"Available Copies : {self.available_copies}")
    def borrow_book(self,quantity):
        if quantity <= 0:
            print("Invalid Quantity")
        elif quantity > self.available_copies:
            print("Not Enough Copies Available")
        else:
            self.available_copies-=quantity
            print(f"{quantity} Books Borrowed Successfully")
            print(f"Remaining Copies  : {self.available_copies}")
    def return_book(self,quantity):
        if quantity <= 0:
            print("Invalid Quantity")
        else:
            self.available_copies+=quantity
            print(f"{quantity} Books Returned Successfully")
            print(f"Available Copies  : {self.available_copies}")
    def update_price(self,new_price):
        self.price = new_price
        print("Price Updated Successfully")
        print(f"New price : {self.price}")
    def book_value(self):
        return self.price * self.available_copies
l = Library("Python","Eric",850,5)
l.display()
l.borrow_book(2)
l.return_book(1)
l.update_price(900)
print(f"Total Book value  : ${l.book_value()}")
l.display()
# 6 --->
class Order:
    def __init__(self,order_id,customer_name,product_name,price,quantity):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.order_status = "Pending"
    def display(self):
        print(f"Order ID      : {self.order_id}")
        print(f"Customer      : {self.customer_name}")
        print(f"Product       : {self.product_name}")
        print(f"Price         : {self.price}")
        print(f"Quantity      : {self.quantity}")
        print(f"Status        : {self.order_status}")
    def total_amount(self):
        return self.price * self.quantity
    def apply_discount(self,percent):
        total = self.total_amount()
        discount = total * percent / 100
        final_amount = total - discount
        return final_amount
    def add_gst(self,percent,discount_percent):
        final_amount = self.apply_discount(discount_percent)
        gst_amount = final_amount * percent / 100
        grand_total = final_amount + gst_amount
        print(f"GST   : ${gst_amount}")
        print(f"Grand Total  : ${grand_total}")
    def confirm_order(self):
        if self.order_status == "Pending":
          self.order_status = "Confirmed"
          print("Order Confirmed Successfully")
        elif self.order_status == "Confirmed":
            print("Order Already Confirmed")
        else:
            print("?")
    def cancel_order(self):
        if self.order_status == "Confirmed":
            self.order_status = "Cancelled"
            print("Order Cancelled Successfully")
        else:
            print("Cannot Cancel Pending Order")
o = Order(101,"Madan","Laptop",500,2)
o.display()
print(o.total_amount())
print(o.apply_discount(10))
o.add_gst(18,10)
o.confirm_order()
o.cancel_order()
o.display()
# 7 --->
class Course:
    def __init__(self,course_name,course_fee,available_seats):
        self.course_name = course_name
        self.course_fee = course_fee
        self.available_seats = available_seats
    def display(self):
        print(f"Course Name     : {self.course_name}")
        print(f"Course Fee      : {self.course_fee}")
        print(f"Available Seats : {self.available_seats}")
class Student:
    def __init__(self,student_name,student_id,balance):
        self.student_name = student_name
        self.student_id = student_id
        self.balance = balance
    def display(self):
        print(f"Student Name    : {self.student_name}")
        print(f"Student Id      : {self.student_id}")
        print(f"Balance         : {self.balance}")
    def enroll(self,course):
        if course.available_seats == 0:
            print("Course Full")
        elif self.balance < course.course_fee:
            print('Insufficient Balance')
        else:
            self.balance-=course.course_fee
            course.available_seats-=1
            print('Enrollment Successful')
    def add_balance(self,amount):
        self.balance+=amount
        print(f"Updated Balance  : {self.balance}")
c = Course('Python',50,2)
madan = Student("Madan",101,70)
dilip = Student("Dilip",102,40)
c.display()
madan.display()
madan.enroll(c)
c.display()
madan.display()
dilip.add_balance(20)
dilip.enroll(c)
c.display()
# CHAPTER C --->  INHERITANCE
# 1 --->
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def display_student(self):
        print(f"Student ID   : {self.student_id}")
s = Student("Madan",19,101)
s.display()
s.display_student()
# 2 --->
class Vehiicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display_vehicle(self):
        print(f"Brand    :{self.brand}")
        print(f"Model    :{self.model}")
class Car(Vehiicle):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
    def display_car(self):
        print(f"Fuel Type   :   {self.fuel_type}")
c = Car("Toyota","Fortuner","Diesel")
c.display_vehicle()
c.display_car()
# 3 --->
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def display_animal(self):
        print(f"Name   : {self.name}")
        print(f"Species: {self.species}")
class Dog(Animal):
    def __init__(self, name, species,sound):
        super().__init__(name, species)
        self.sound = sound
    def bark(self):
        print(f"Tommy says {self.sound}")
d = Dog("Tommy","Dog","Woof Woof")
d.display_animal()
d.bark()
#4 --->
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_employee(self):
        print(f"Name     : {self.name}")
        print(f"Salary   : {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def display_manager(self):
        print(f"Department   : {self.department}")
m = Manager("Madan",49,"IT")
m.display_employee()
m.display_manager()
# 5 --->
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
class Employee(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary
    def display_employee(self):
        print(f"Salary  : ₹{self.salary}")
class Manager(Employee):
    def __init__(self, name, age, salary,department):
        super().__init__(name, age, salary)
        self.department = department
    def display_manager(self):
        print(f"Department   : {self.department}")
m = Manager("Madan",30,50000,"IT")
m.display_person()
m.display_employee()
m.display_manager()
# 6 --->
class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} says Woof Woof")
d = Dog("Tommy")
d.make_sound()
# 7 --->
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name    : {self.name}")
        print(f"Salary  : {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        super().display()
        print(f"Department  : {self.department}")
m = Manager("K.Madan Kumar",50000,"IT")
m.display()
# 8 --->
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed
    def dog_info(self):
        print(f"Breed   : {self.breed}")
class Cat(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
    def cat_info(self):
        print(f"Color   : {self.color}")
d = Dog("Chimtu",3,"Kukka")
c = Cat("Pilli",2,"White")
d.display()
d.dog_info()
c.display()
c.cat_info()
# 9 --->
class Father:
    def __init__(self,father_name):
        self.father_name = father_name
    def father_info(self):
        print(f"Father   : {self.father_name}")
class Mother:
    def __init__(self,mother_name):
        self.mother_name = mother_name
    def mother_info(self):
        print(f"Mother   : {self.mother_name}")
class Child(Father,Mother):
    def __init__(self, father_name,mother_name,child_name):
        Father.__init__(self,father_name)
        Mother.__init__(self,mother_name)
        self.child_name = child_name
    def child_info(self):
        print(f"Child  : {self.child_name}")
c = Child("Ram","Sita","Lava Kusa")
c.father_info()
c.mother_info()
c.child_info()
# 10 --->
class Account:
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def display(self):
        print(f"Account Number   : {self.account_number}")
        print(f"Holder Name      : {self.holder_name}")
        print(f"Balance          : {self.balance}")
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            self.balance+=amount
            print(f"{amount} Deposited Successfully")
    def withdrawn(self,amount):
        if amount <= 0:
            print("Invalid Amount")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"{amount} Withdrawn Successfully")
class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance,interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest    :  {interest}")
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance+=interest
        print("Interest Added Successfully")
        print(f"Current balance    : {self.balance}")
s = SavingsAccount(1001,"K.Madan Kumar",1000,5)
s.display()
s.deposit(200)
s.withdrawn(100)
s.calculate_interest()
s.add_interest()
s.display()
# 11 --->
class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
    def display_user(self):
        print(f"User ID  : {self.user_id}")
        print(f"Name     : {self.name}")
class Customer(User):
    def __init__(self, user_id, name,cart_value,membership):
        super().__init__(user_id, name)
        self.cart_value = cart_value
        self.membership = membership
    def display_customer(self):
        print(f"Cart Value   : {self.cart_value}")
        print(f"MemberShip   : {self.membership}")
    def apply_discount(self):
        if self.membership == "Silver":
            discount = 5
        elif self.membership == "Gold":
            discount = 10
        elif self.membership == "Platinum":
            discount = 20
        else:
            discount = 0
        discount_amount = self.cart_value * discount / 100
        final_amount = self.cart_value - discount_amount
        return final_amount
    def add_gst(self):
        amount = self.apply_discount()
        gst = amount * 18 / 100
        grand_total = amount + gst
        print(f"GST         : {gst}")
        print(f"Grand Total : {grand_total}")
c = Customer(101,"Madan",5000,"Gold")
c.display_user()
c.display_customer()
amount = c.apply_discount()
print(f"Amount After Discount  : ₹{amount}")
c.add_gst()