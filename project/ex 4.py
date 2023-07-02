# initialize sum and list of numbers
sum = 0
numbers = []

# find numbers not divisible by 2, 3 or 5
for i in range(1, 21):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        numbers.append(i)
        sum += i

# print the list of numbers and the sum
print("Numbers from 1 to 20 which are not divisible by 2, 3, and 5:")
for number in numbers:
    print(number)

print("Sum of numbers from 1 to 20 which are not divisible by 2, 3 or 5 is =", sum)