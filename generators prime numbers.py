"""
Write a Python program that creates a generator 
function that generates all prime numbers between two given numbers. 
"""
import sys
def prime(x,y):
    while x<y:
        count=0
        for i in range(2,x):
            if x%i==0:
                count+=1
                break
        if count==0:
            yield x        
        x+=1
# ####
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
obj=prime(x,y)
print(sys.getsizeof(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
