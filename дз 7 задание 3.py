class Cell:
    def __init__(self, y):
        self.y = y

    def __str__(self):
        return f"{self.y}"

    def __add__(self, other):
        return Cell(self.y + other.y)

    def __sub__(self, other):
        if int(str(Cell(self.y - other.y))) > 0:
            return Cell(self.y - other.y)
        else:
            return f'Некорретная операция'

    def __mul__(self, other):
        return Cell(self.y * other.y)

    def __floordiv__(self, other):
        return Cell(self.y // other.y)

    def make_order(self, n):
        z = self.y // n
        p = '*'
        print((f'{p * n}\n') * z, end='')
        print(f'{p * (self.y - n * z)}')


cell_1 = Cell(7)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_2 // cell_1)
cell_1.make_order(3)
print()
cell_2.make_order(3)
