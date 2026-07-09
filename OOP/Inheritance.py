#  INHERITANCE = Inheritance means one class acquires the properties and methods of another class
#            OR = One class takes the features of another class
# Ex : 
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
d = Dog()
d.eat()   # ---> Eating
# SINGLE INHERITANCE = Single Inheritance occurs when one child class  inherits from one parent class
# Ex : 
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
d = Dog()
# MULTILEVEL INHERITANCE
# Ex : 
class Animal:
    def eat(self):
        print("Eating")
class Mammal(Animal):
    def walk(self):
        print("Walking")
class Dog(Mammal):
    def bark(self):
        print("Barking")
d = Dog()
d.eat()
d.walk()
d.bark()
# MULTIPLE INHERITANCE = One Child Has Multiple Parents
# Ex :
class Father:
    def money(self):
        print("Father's Money")
class Mother:
    def love(self):
        print("Mother's Love")
# class Child(Father,Mother):
class Child(Mother,Father):
    pass
c = Child()
c.money()
c.love()
# HIERARCHICAL INHERITANCE = One Parent Has Multiple Children
# Ex : 
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
d = Dog()
c = Cat()
d.eat()
c.eat()
# SUPER FUNCTION = Is Used to call the parent class methods or constructor from child class
# Ex : 
class Animal:
    def __init__(self):
        print("Animal Constructor")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")
d = Dog()
# PROBLEMS
# 1 --->
class Person:
    def speak(self):
        print("Person Can Speak")
class Student(Person):
    pass
s = Student()
s.speak()
# 2 --->
class Animal:
    def eat(self):
        print("Animal Is Eating")
class Dog(Animal):
    def bark(self):
        print("Dog Is Barking")
d = Dog()
d.eat()
d.bark()
# 3 ---> 
class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    def drive(self):
        print("Car Is Driving")
class SportsCar(Car):
    def turbo(self):
        print("Car Activated Turbo Mode")
c = SportsCar()
c1 = Car()
c.start()
c.drive()
c.turbo()
c1.start()
c1.drive()
# 4 ---> 
class School:
    def school_name(self):
        print("Govt.High School")
class Classroom(School):
    def room_num(self):
        print("Room Number = 7")
class Student(Classroom):
    def student_name(self):
        print("Student's Name = K.Madan Kumar")
s = Student()
s.school_name()
s.room_num()
s.student_name()
# 5 --->
class Shape:
    def display(self):
        print("This Is A Shape")
class Rectangle(Shape):
    def rectangle_Area(self):
        print("Area Of Rectangle = length * breadth")
class Square(Rectangle):
    def square_Area(self):
        print("Square Area = Sie * Side")
s = Square()
s.display()
s.rectangle_Area()
s.square_Area()
# 6 ---> 
class Father:
    def money(self):
        print("Father's money")
class Mother:
    def care(self):
        print("Mother's Love")
class Child(Father,Mother):
    pass
c = Child()
c.money()
c.care()
# 7 ---> 
class Camera:
    def take_photo(self):
        print("Photo Captures")
class Phone:
    def call(self):
        print("Calling")
class SmartPhone(Camera,Phone):
    pass
s = SmartPhone()
s.take_photo()
s.call()
# 8 --->
class Animal:
    def eat(self):
        print("Animal Is Eating")
class Dog(Animal):
    def bark(self):
        print("Dog Is Barking")
class Cat(Animal):
    def meow(self):
        print("Cat Is Meowing")
class Cow(Animal):
    def moo(self):
        print("Cow Is Mooing")
d = Dog()
d.eat()
d.bark()
   