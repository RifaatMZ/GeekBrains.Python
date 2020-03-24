class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car is moving!")

    def stop(self):
        print("Car stopped!")

    def turn(self, direction):
        self.direction = direction
        print(f"The car turned {direction}!")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def car_class(self):
        return type == "town_car"

    def show_speed(self):
        if self.speed > 60:
            print("Over speed limit!")
        else:
            print(self.speed)



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Over speed limit!")
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


VW = TownCar(51, "Red", "Polo", False)
PC = PoliceCar(100, "Black", "Mustang", True)
Skoda = WorkCar(41, "Red", "Polo", False)
Tesla = SportCar(180, "Yellow", "Model S", False)


Skoda.go()
VW.stop()
PC.turn("left")
VW.show_speed()
PC.show_speed()
Skoda.show_speed()
Tesla.show_speed()