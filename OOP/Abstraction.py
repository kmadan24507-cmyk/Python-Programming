# ABSTRACTION = Abstraction is the process of hiding implementation details and showing only the essential features of object.
# The User Know what to do but did not know how it's done
# abc = Abstract Base Class
# @abstractmethod = Abstract Method
# Ex : 
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
d = Dog()
d.sound()
# PROBLEMS
# 1 --->
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Starts")
c = Car()
c.start()
# 2 --->
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    def sleep(self):
        print("Animal Is Sleeping")
class Dog(Animal):
    def sound(self):
        print('Dog Barks')
    def eat(self):
        print("Dog Eat Meats")
d = Dog()
d.sound()
d.eat()
d.sleep()
# 3 --->
from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass
    def display(self):
        print(f"Animal Name = {self.name}")
class Dog(Animal):
    def sound(self):
        print(f"{self.name} Barks")
d = Dog("Chimtu")
d.sound()
d.display()
# 4 --->
from abc import ABC,abstractmethod
class Person(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
class Student(Person):
    @property
    def name(self):
        return "Madan"
s = Student()
print(s.name)
# 5 --->
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @classmethod
    @abstractmethod
    def info(self):
        pass
class Car(Vehicle):
    @classmethod
    def info(self):
        print("This Is A Car")
Car.info()