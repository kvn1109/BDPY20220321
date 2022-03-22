import decimal
from decimal import Decimal
from decimal import Decimal as Dec
print(Decimal(2.968))
print(Decimal('2.968'))
print(Decimal(2968) * Decimal('0.001') - Decimal(2.968))
print(Decimal(2968) * Decimal('0.001') - Decimal('2.968'))
print(Dec(3.968))
print(decimal.Decimal(4.968))