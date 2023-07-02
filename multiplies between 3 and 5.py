x=-1
while x<1 or x>100: 
    x=int(input("please enter numbe bettween 1 and 100:"))
    if x<1 or x>100:
        print("your is not included in range [1:100]")
for i in range(1,x+1):
    if i%3==0:
        print("Three")
    if i%5==0:
        print("Five")
    if i%5==0 and i%3==0:
        print("Three-Five")
