import sys
import itertools
def permut(lst):
    permutations = itertools.permutations(lst)
    for permutation in permutations:
        yield list(permutation)
#object
obj=permut([1,2,3,8,9,7])
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(sys.getsizeof(obj))