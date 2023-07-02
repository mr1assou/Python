"""
Write a Python program that creates a 
generator that generates all prime factors of a given number. 
"""
from sys import getsizeof
def prime_factors(n):
    for i in range(1,n):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0 and n%i==0:
            yield i
#### object code
obj=prime_factors(36)
for i in obj:
    print(i)
print(getsizeof(obj)) 