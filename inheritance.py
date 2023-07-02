class food:
    def __init__(self,name,price,amount) -> None:
        self.name=name
        self.price=price
        self.amount=amount
        print(f"the of food inside base class is {self.name}")
    def eat(self):
        print("eat method from base class")
class apple(food):
    def __init__(self,name,price,amount) -> None:
        food.__init__(self,name,price,amount)
        #super().__init__(name,price,amount)
        print(f"apple is created inside derived class the name is {self.name} and price is {self.price}$ amount is {self.amount}")
    def display(self):
            print("hello my name is marwane inside derived class")
    def eat(self):
        print("eat method from derived class")
obj1=apple("apple","90","3000")
print(obj1.eat())