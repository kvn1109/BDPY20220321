class Person:
        def __init__(self, age):
            self.age = age
            pass
        pass

p1 = Person(5)
x = 5
print(f"p1 id = {hex(id(p1))},x id = {hex(id(x))}")
print(f"p1.age id = {hex(id(p1))}")
p1.age = 6