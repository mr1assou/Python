def running_average_generator():
    total = 0
    count = 0
    while True:
        value = yield total / count if count > 0 else 0
        total += value
        count += 1
####
running_avg_gen = running_average_generator()
#start generator to avoid zero and stop in yield
next(running_avg_gen)
while True:
    num = float(input("enter a number:"))
    value= num
    average = running_avg_gen.send(value) #value assign to variable ledt hand of yield
    print(average)