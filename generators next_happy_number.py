"""
Write a Python program to 
implement a generator that generates the next happy number after a given number. 
"""
import sys
def happy_number(n):
    lst=[]
    while True: 
        n=n+1
        p=n
        n=str(n)
        total=0
        while total!=1:
            total=sum((int(i)**2 for i in n))
            n=str(total)
            if total in lst:
                break
            else:
                lst.append(total)
        if total==1:
            yield f"the number {p} is happy"
        else:
            yield f"the number {p} is not happy"
        n=p
#object
obj=happy_number(10000)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(sys.getsizeof(obj))