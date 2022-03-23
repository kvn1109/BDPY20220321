class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # width = self.width
        # height = self.height

    def calculate_area(self):
        return self.width * self.height


r1 = Rectangle(3, 4)
print(f'r1 area={r1.calculate_area()}')
r2 = Rectangle(4, 5)
print(f"r2 area={r2.calculate_area()}")