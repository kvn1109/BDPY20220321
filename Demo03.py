from fractions import Fraction

f1 = Fraction(250, 72)
print(f1)
f2 = Fraction(369,12)
print(f2)
f3 = f1 + f2
print(type(f3), f3.denominator, f3.numerator)
f4 = Fraction(1357, 246) + Fraction(2468, 135)
print(f4)