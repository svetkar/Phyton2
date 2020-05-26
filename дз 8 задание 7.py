class ComplexNumber:
    def __init__(self, a, b):
        self.num = complex(a, b)
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


num_1 = ComplexNumber(2, 3)
print(f'Первое комплексное число: {num_1}')
num_2 = ComplexNumber(1, 4)
print(f'Второе комплексное число: {num_2}')
print(f'Сумма этих чисел: {num_1 + num_2}')
print(f'Произведние этих чисел: {num_1 * num_2}')
