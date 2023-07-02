"""
Write a Python program to implement 
a generator function that generates the Fibonacci sequence. 
"""
def fibonacci(n):
    a=0
    b=1
    while a<n: 
        a,b=b,a+b
        yield a
obj=fibonacci(15)
for i in obj:
    print(i)