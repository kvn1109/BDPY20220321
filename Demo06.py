class Foo()：
    def __str__(self):
        return "Foo in str format"

    def __repr__(self):
        return "Foo in repr format"

f1 = Foo()
print(f1)