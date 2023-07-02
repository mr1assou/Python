"""
Write a Python program to implement a generator 
that generates the Collatz sequence for a given number. 
"""
from sys import getsizeof
def collatz_sequence(n):
    yield n
    while n!=1:
        if n%2==0:
            yield n//2
            n=n//2
        else:
            n=n*3+1
            yield n
obj=collatz_sequence(1000)
for i in obj:
    print(i,end=' ')
print()
print(getsizeof(obj))