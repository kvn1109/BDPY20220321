
class MyClass:
    pass

m1 = MyClass()

class MySubClass(MyClass):
    pass

m2 = MySubClass()

print(type(MyClass), type(m1).__name__)
print(m1.__class__, m1.__class__ == MyClass)
print(m1.__class__.__base__)
print(m2.__class__.__base__)