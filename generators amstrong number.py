"""
Write a Python program to implement a generator that generates the 
next Armstrong number after a given number. 
"""
def amstrong_number(n):
    while True:
        p=n
        n=str(n)
        result=sum((int(i)**3 for i in n))
        if result==p:
            yield f"the number {p} is amstrong"
        else:
            yield f"the number {p} is not amstrong"
        n=p+1
###
obj=amstrong_number(370)
print(next(obj))
print(next(obj))
print(next(obj))