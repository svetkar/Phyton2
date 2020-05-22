from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 54:
            self.__size = 54
        else:
            self.__size = size

    def expances(self, q):
        return f'Размер пальто {str(self.size)}, план производства {q} шт.Расход ткани: {(int(str(self.size)) / 6.5 + 0.5) * q:.02f}'

    def expances1(self, q):
        return (int(str(self.size)) / 6.5 + 0.5) * q


class Suite(Clothes):
    def __init__(self, name, tall):
        super().__init__(name)
        self.tall = tall

    @property
    def tall(self):
        return self.__tall

    @tall.setter
    def tall(self, tall):
        if tall < 160:
            self.__tall = 160
        elif tall > 210:
            self.__tall = 210
        else:
            self.__tall = tall

    def expances(self, q):
        return f'Костюм расчитан на рост {str(self.tall)} см, план производства {q} шт. Расход ткани: {(int(str(self.tall)) * 2 + 0.3) * q:.02f} '

    def expances1(self, q):
        return (int(str(self.tall)) * 2 + 0.3) * q


coat_1 = Coat('Trench', 44)
print(coat_1.name)
print(coat_1.expances(100))
print()
suite_1 = Suite('Sara', 165)
print(suite_1.name)
print(suite_1.expances(50))
print()
print(f'Oбщий расход ткани {suite_1.expances1(50) + coat_1.expances1(100):.02f}')
print()
coat_2 = Coat('Trench_big', 58)
print(coat_2.name)
print(coat_2.expances(10))
print()
suite_2 = Suite('Sara_small', 150)
print(suite_2.name)
print(suite_2.expances(10))
print()
print(f'Oбщий расход ткани {suite_1.expances1(50) + coat_1.expances1(100) + suite_2.expances1(10) + coat_2.expances1(10):.02f}')