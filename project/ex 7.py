# Write a function histogram that takes string as parameter and generates a
# frequency of characters contained in it.
# S = "AAPPLE"
# The program should create a dictionary
# D = {'A': 2, 'E': 1, 'P': 2, 'L': 1}
# Output:
# {'A': 2, 'P': 2, 'L': 1, 'E': 1}
def apple(y):
    dictionary={}
    for i in y:
        if i not in dictionary:
            dictionary[i]=1
        else:
            dictionary[i]+=1
    return dictionary

s = "AAPPLE"
print(apple(s))