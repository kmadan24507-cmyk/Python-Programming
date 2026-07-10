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