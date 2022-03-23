class Car:
    vendor = 'BMW'
    valid = True


c1 = Car()
c2 = Car()
print(Car.vendor, c1.vendor, c2.vendor)
Car.vendor = "Toyota"
print(Car.vendor, c1.vendor, c2.vendor)
c1.vendor = "Nissan"
print(Car.vendor, c1.vendor, c2.vendor)
c1.passengers = 5
c2.color = 'red'
print(c1.vendor, c1.valid, c1.passengers)
print(c2.vendor, c2.valid, c2.color, Car.valid)