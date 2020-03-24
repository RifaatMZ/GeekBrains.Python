class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self, thickness):
        return f"{self.length * self.width * (thickness / 100) * 25} kgs"


m5 = Road(3000, 20)
print(m5.mass(10))

