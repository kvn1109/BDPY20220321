from itertools import chain, permutations, combinations
from pprint import pprint

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
c1 = chain(l1, l2, l3)
print(c1)
print([c for c in c1])
print([c for c in c1])
c2 = tuple(chain(l1, l2, l3, l1))
print([c for c in c2])
print([c for c in c2])
print([c for c in c2])
stores = ['7-11', 'mos', 'fami', 'mac', 'kfc', 'starbucks']
pprint(tuple(permutations(stores, 2)))
print("---"*30)
pprint(tuple(combinations(stores, 2)))