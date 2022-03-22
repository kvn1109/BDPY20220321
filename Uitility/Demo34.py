def foo(a, b):
    return f"a+b={100+a + b}"


def bar(a, b):
    return f"a*b={100*a * b}"

if __name__ == '__main__':
    print("==Demo34==")
    print(foo(1, 2))
    print(bar(3, 4))