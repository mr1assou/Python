class baseone:
    def __init__(self,name) -> None:
        self.name=name
class basetwo:
    def __init__(self,age) -> None:
        self.age=age
class derived(baseone,basetwo):
    def __init__(self,name,age) -> None:   
        baseone.__init__(self,name)
        basetwo.__init__(self,age)
    def set_display(self):
        print(f"the age is {self.name} and {self.age}")
my_var=derived("marwane",19)
my_var.set_display()

