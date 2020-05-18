class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        w_for_1m2 = 25 #килограммы
        cm_tol = 5 #сантиметры
        w = self._length*self._width*w_for_1m2*cm_tol / 1000
        print(f'Масса асфальта {w:.2f} т.')

road_1 = Road(35, 7)
road_1.weight()
