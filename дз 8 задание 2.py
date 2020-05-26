class OwnError(Exception):
    def __init__(self, txt):
        self.t = txt


a = input('Введите делимое: ')
b = input('Введите делитель: ')
try:
    b = int(b)
    if b == 0:
        raise OwnError('Деление на ноль невозможно!')
except ValueError:
    print(f'Введены неверные значения.')
except OwnError as err:
    print(err)
else:
    try:
        a = int(a)
    except ValueError:
        print(f'Введены неверные значения.')
    else:
        print(f'{(int(a) / int(b)):.02f}')
