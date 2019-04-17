class TownCar:
    def __init__(self):
        self.speed = '60-80 km/h'
        self.colour = 'blue'
        self.name = 'town'
        self.is_police = ''
    def police(self):
        return print(bool(self.is_police))
    def go(self):
        print('car starts to move')
    def stop(self):
        print('car stops')
    def turn(self, direction):
        print('Car turns ', direction)
class SportCar(TownCar):
    def __init__(self):
        self.speed = '120-150 km/h'
        self.colour = 'red'
        self.name = 'Sport'
        self.is_police = ''
class WorkCar(TownCar):
    def __init__(self):
        self.speed = '80-100 km/h'
        self.colour = 'black'
        self.name = 'Work'
        self.is_police = ''
class PoliceCar(TownCar):
    def __init__(self):
        self.speed = '100-120 km/h'
        self.colour = 'grey'
        self.name = 'Police'
        self.is_police = 'is a police car'

my_car1 = TownCar()
my_car2 = SportCar()
my_car3 = WorkCar()
my_car4 = PoliceCar()
