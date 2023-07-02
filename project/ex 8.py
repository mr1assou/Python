# define the number of rows
num_rows = 5

# loop through each row
for i in range(1, num_rows+1):
    # print numbers for each row
    for j in range(1, i+1):
        print(j, end=" ")
    print()