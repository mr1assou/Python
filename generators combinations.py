import sys
import itertools
def permut(lst):
    combinations = itertools.combinations(lst,4)
    for combination in combinations:
        yield list(combination)
#object
obj=permut([1,2,3,4,5])
print(next(obj))
print(next(obj))
print(next(obj))

print(sys.getsizeof(obj))