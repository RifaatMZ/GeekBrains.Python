import time


class TrafficLight:

    def __init__(self, color):
        self._color: str = color

    def running(self):
        while True:
            if 'Red' in self._color or 'red' in self._color:
                print("Reeed!!")
                time.sleep(7)
                self._color = 'Yellow'
            elif 'Yellow' in self._color or 'yellow' in self._color:
                print("Yellowww!!")
                time.sleep(2)
                self._color = 'Green'
            elif 'Green' in self._color or 'green' in self._color:
                print("Greeeen!!")
                time.sleep(5)
                self._color = 'Red'
            else:
                print("Broken")
                break


light = TrafficLight("red")
light.running()
