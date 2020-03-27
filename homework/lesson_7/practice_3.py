class Cell:

    def __init__(self, n):
        self.n = int(n)

    def __add__(self, other):   # (self, other) - сложение. x + y вызывает x.__add__(y)
        return self.n + other.n

    def __sub__(self, other):   # (self, other) - вычитание (x - y).
        return abs(self.n - other.n)

    def __mul__(self, other):   # (self, other) - умножение (x * y).
        return self.n * other.n

    def __truediv__(self, other):   # (self, other) - деление (x / y).
        if self.n > other.n:
            return round(self.n / other.n)
        else:
            return round(other.n / self.n)

    def make_order(self, count):
        line = ""
        i = self.n / count
        j = self.n % count
        while i > 2:
            line += f"{count *'*'}" r"\n"
            i -= 1
        line += f"{count *'*'}"
        if j:
            line += r"\n"
            line += f"{j *'*'}"
        print(line)


red = Cell(5)
white = Cell(20)
neuron = Cell(19)
muscle = Cell(9)

cell_1 = Cell.__add__(red, white)
cell_2 = Cell.__truediv__(white, neuron)
cell_3 = Cell.__truediv__(white, muscle)
print(cell_1)
print(cell_2)
print(cell_3)

neuron.make_order(5)



