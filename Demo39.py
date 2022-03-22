import math
import random

print(math.pi, math.log2(8), math.log10(3))
print(math.sqrt(5), math.sqrt(50))
for _ in range(100):
    print(random.randint(1, 10), end=" ")
print()
stores = ['7-11', 'mac', 'kfc', 'sb', 'fami']
print(random.choice(stores))
cards = ['A', "K", 'Q', 'J', 10]
for _ in range(10):
    random.shuffle(cards)
    print(cards)
print("The End")