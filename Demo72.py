import pprint

def fib(max):
    prev, current = 0, 1
    count = 0
    while count < max:
        count += 1
        yield current
        #費氏計算排列，第三項等於前兩項的和，以此類推
        prev, current = current, current + prev
        pass
    pass

print([x for x in fib(100)])
#pprint([x for x in fib(100)])