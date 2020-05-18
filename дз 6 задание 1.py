import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            1 == 1
            self.__color = 'Red'
            print(f'\033[31m {self.__color}')
            time.sleep(7)
            self.__color = 'Yellow'
            print(f'\033[33m {self.__color}')
            time.sleep(2)
            self.__color = 'Green'
            print(f'\033[32m {self.__color}')
            time.sleep(7)
            self.__color = 'Yellow'
            print(f'\033[33m {self.__color}')
            time.sleep(2)


tl_1 = TrafficLight('Black')
tl_1.running()
