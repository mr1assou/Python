num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))
num3 = float(input("Enter the third Number: "))
num4 = float(input("Enter the fourth Number: "))

# find the largest number among the four numbers
largest = num1

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

if num4 > largest:
    largest = num4

# print the sum and largest number
print("The largest number is =", largest)