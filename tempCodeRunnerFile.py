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