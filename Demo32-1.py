import Demo32
import Uitility.Demo34
import Uitility.Output.Demo35

print("===Demo32-1===")

print(Demo32.foo(5, 6))
print(Demo32.bar(7, 8))
print(Uitility.Demo34.foo(9, 10))
print(Uitility.Demo34.bar(11, 12))

from Demo32 import foo, bar

print("way2----")
print(foo(13, 14))
print(bar(15, 16))
from Uitility.Demo34 import foo as f2
from Uitility.Demo34 import bar as b2

print(f2(17, 18))
print(b2(19, 20))