class Worker:
    def __init__(self,name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def my_dict(self):
        return {"Wage: ": self._income * 0.8, "Bonus: ": self._income * 0.2}


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income


someone = Position("Name", "Surname", "Engineer", 30000)

print(Position.get_full_name(someone))
print(Position.get_total_income(someone))