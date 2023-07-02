# take input from the user
first_num = int(input("Please enter First Number: "))
second_num = int(input("Please enter Second Number: "))
num_terms = 8

# initialize the series
fib_series = [first_num, second_num]

# generate the Fibonacci series
for i in range(2, num_terms):
    next_num = fib_series[i-1] + fib_series[i-2]
    fib_series.append(next_num)

# print the series
print("Fibonacci Series =", end=" ")
for num in fib_series:
    print(num, end=" ")