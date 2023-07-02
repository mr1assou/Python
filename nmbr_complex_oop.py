from math import sqrt
class complex:
    x=1
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        if complex.x==1:
            print(f"The first Complex Number is as Follows: ({self.real},{self.imag})")
            complex.x+=1 
        elif complex.x==2:
            print(f"The second Complex Number is as Follows: ({self.real},{self.imag})") 
    def __add__(self,other):
        return f"({(self.real+other.real)},{(self.imag+other.imag)})"
    def __sub__(self,other): 
        return f"({(self.real-other.real)},{(self.imag-other.imag)})"
    def __mul__(self,other):
        return f"({(self.real*other.real)-(self.imag*other.imag)},{(self.real*other.imag)+(self.imag*other.real)})"    
    def __eq__(self,other):
        if self.real==other.real and self.imag==other.imag:
            return True
        else:
            return False
    def __le__(self,other):
        if sqrt((self.real**2)+(self.imag**2))<sqrt((other.real**2)+(other.imag**2)):
            return True
        else:
            return False
    def __ge__(self,other):
        if  sqrt(self.real**2+self.imag**2)>sqrt(other.real**2+other.imag**2):
            return True
        else:
            return False
#create object
obj1=complex(1,9)
obj2=complex(4,5)
print(obj1+obj2)

