from abc import ABC, abstractmethod


class Clothes(ABC):
    _total_material = 0

    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    _total_material = 0

    def __init__(self, size):
        self.size = float(size)

    @property
    def consumption(self):
        consumption = (self.size / 6.5) + 0.5
        Coat._total_material += consumption
        Clothes._total_material += consumption
        return "%.2f" % consumption


class Suit(Clothes):
    _total_material = 0

    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        consumption = (self.height * 2) + 0.3
        Suit._total_material += consumption
        Clothes._total_material += consumption
        return "%.2f" % consumption


a = Coat(5)
b = Suit(5)
c = Coat(10)

print(a.consumption)
print(b.consumption)
print(c.consumption)
print("%.2f" % Coat._total_material)
print("%.2f" % Clothes._total_material)

