class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'Машина тронулась.')

    def stop(self):
        print(f'Машина остановилась.\n')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость движения: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'\033[31mПревышение скорости!\033[0m')
        else:
            print(f'Скорость движения: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'\033[31mПревышение скорости!\033[0m')
        else:
            print(f'Скорость движения: {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car_1 = TownCar(40, 'red', 'Reno', 0)
print(
    f'Характеристики машины: скорость: {town_car_1.speed}, цвет: {town_car_1.color}, название: {town_car_1.name}, полицейская или нет: {town_car_1.is_police}')
town_car_1.go()
town_car_1.show_speed()
town_car_1.turn('направо')
town_car_1.stop()

town_car_2 = TownCar(70, 'black', 'Toyota', 0)
print(
    f'Характеристики машины: скорость: {town_car_2.speed}, цвет: {town_car_2.color}, название: {town_car_2.name}, полицейская или нет: {town_car_2.is_police}')
town_car_2.go()
town_car_2.show_speed()
town_car_2.turn('налево')
town_car_2.stop()

work_car_1 = WorkCar(40, 'yellow', 'Liebherr', 0)
print(
    f'Характеристики машины: скорость: {work_car_1.speed}, цвет: {work_car_1.color}, название: {work_car_1.name}, полицейская или нет: {work_car_1.is_police}')
work_car_1.go()
work_car_1.show_speed()
work_car_1.turn('налево')
work_car_1.stop()

work_car_2 = WorkCar(50, 'Grey', 'ABEL', 0)
print(
    f'Характеристики машины: скорость: {work_car_2.speed}, цвет: {work_car_2.color}, название: {work_car_2.name}, полицейская или нет: {work_car_2.is_police}')
work_car_2.go()
work_car_2.show_speed()
work_car_2.turn('налево')
work_car_2.stop()

sport_car_1 = SportCar(100, 'yellow', 'Ferrari', 0)
print(
    f'Характеристики машины: скорость: {sport_car_1.speed}, цвет: {sport_car_1.color}, название: {sport_car_1.name}, полицейская или нет: {sport_car_1.is_police}')
sport_car_1.go()
sport_car_1.show_speed()
sport_car_1.turn('направо')
sport_car_1.stop()

police_car_1 = PoliceCar(40, 'blue', 'Mercedes-Benz', 1)
print(
    f'Характеристики машины: скорость: {police_car_1.speed}, цвет: {police_car_1.color}, название: {police_car_1.name}, полицейская или нет: {police_car_1.is_police}')
police_car_1.go()
police_car_1.show_speed()
police_car_1.turn('направо')
police_car_1.stop()
