number = int(input("Please enter the number: "))

# initialize sum and number of digits
sum = 0
num_digits = len(str(number))

# calculate sum of cube of each digit
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

# check if number is Armstrong or not
if number == sum:
    print("The number", number, "is Armstrong Number")
else:
    print("The number", number, "is not Armstrong Number")