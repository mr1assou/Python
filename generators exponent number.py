"""
Write a Python program to create a generator function that generates 
the powers of a number up to a specified exponent. 
"""
def power_exponent(n,exp):
    for i in range(exp+1):
        yield n**i
obj=power_exponent(8,4)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))