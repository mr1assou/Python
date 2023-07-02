"""
Write a Python program to create a 
generator function that generates all factors of a given number. 
"""
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
obj=factors(2)
for i in obj:
    print(i)