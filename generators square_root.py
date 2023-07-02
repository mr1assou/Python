"""
Write a Python program to create a generator 
that generates the square, cube roots of numbers from 1 to n. 
"""
import math,sys
def root_number_square(n):
    for i in range(n+1):
        yield f"the square of number {i**2} and the roots {math.sqrt(i):.2f}"
####
obj=root_number_square(6)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))