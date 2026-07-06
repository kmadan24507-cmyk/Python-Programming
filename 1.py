# 7 --->
class Student:
    def __init__(self):
        self.__marks = 0
    @property      # PROPERTY GETTER
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
class Student:
    def __init__(self):
        self.__marks = 0
      