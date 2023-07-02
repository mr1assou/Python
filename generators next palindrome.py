"""
Write a Python program that creates a generator 
function that generates the next palindrome number
after a given number. 
"""
import sys
def next_palindrome(n):
    count=-1
    n=n+1
    while count!=0:
        p=n
        r=0
        while n!=0:
            r=r*10+n%10
            n=n//10
        if n==0 and p==r:
            count+=1
            yield f"the number is PALINDROME {p}"
        n=p+1
obj=next_palindrome(1000)
for i in obj:
    print(i)

