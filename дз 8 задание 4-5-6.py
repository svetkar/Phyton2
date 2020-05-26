class Sklad:
    def __init__(self, zapas):
        self.zapas = zapas

    def __str__(self):
        return f'Складские запасы: {self.zapas}'

    def priem(self, orgtech_name, q):
        l = self.zapas.get(orgtech_name)
        m = q + l
        self.zapas.update({orgtech_name: m})

    def peremeschenie(self, orgtech_name, q, otdel_number, otdely):
        l = self.zapas.get(orgtech_name)
        m = l - q
        self.zapas.update({orgtech_name: m})
        t = otdely.get(otdel_number)
        c = t.get(orgtech_name)
        s = c + q
        t.update({orgtech_name: s})
        otdely.update({otdel_number: t})

    def spisanie(self, orgtech_name, q):
        l = self.zapas.get(orgtech_name)
        m = l - q
        self.zapas.update({orgtech_name: m})


class Orgtech:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price


class Printer(Orgtech):
    def __init__(self, name, model, price, color_or_black):
        super().__init__(name, model, price)
        self.color_or_black = color_or_black


class Scanner(Orgtech):
    def __init__(self, name, model, price, potok_or_page):
        super().__init__(name, model, price)
        self.potok_or_page = potok_or_page


class Xerox(Orgtech):
    def __init__(self, name, model, price, A3_or_A4):
        super().__init__(name, model, price)
        self.A3_or_A4 = A3_or_A4


def proverka_2(i):
    if i == 1:
        return 'printer'
    if i == 2:
        return 'scanner'
    if i == 3:
        return 'xerox'
    else:
        return 4


sklad_1 = Sklad({'printer': 10, 'scanner': 15, 'xerox': 5})
print(sklad_1)
otdely = {1: {'printer': 1, 'scanner': 2, 'xerox': 1}, 2: {'printer': 1, 'scanner': 1, 'xerox': 2}}
print(f'Запасы в отделах: {otdely}')
sklad_1.priem('printer', 2)
print(f'На склад поступили 2 новых принтера: {sklad_1}')
sklad_1.peremeschenie('scanner', 1, 1, otdely)
print('Со склада в отдел 1 перемещен 1 сканер')
print(sklad_1)
print(f'Запасы в отделах: {otdely}')
sklad_1.spisanie('xerox', 3)
print('Со склада списаны 3 ксерокса.')
print(sklad_1)
print()
q1 = input('Хотите принять оргтехнику на склад? Да - нажмите 1, Нет - 2: ')
while True:
    try:
        if int(q1) == 1:
            try:
                q2 = int(input('Выберите наименование: 1 - принтер, 2 - сканер, 3 - ксерокс: '))
                if proverka_2(q2) != 4:
                    try:
                        q3 = int(input('Введите количество: '))
                        sklad_1.priem(proverka_2(q2), q3)
                        print(sklad_1)
                        q1 = input('Хотите принять оргтехнику на склад? Да - нажмите 1, Нет - 2: ')
                    except ValueError:
                        print(f'Введено некорректное значение!')
                if proverka_2(q2) == 4:
                    print(f'Введено некорректное значение!')
            except ValueError:
                print('Введено некорректное значение!')
        if int(q1) == 2:
            break
        if int(q1) != 1 and int(q1) != 2:
            print('Введено некорректное значение!')
            q1 = input('Хотите принять оргтехнику на склад? Да - нажмите 1, Нет - 2: ')
    except ValueError:
        print('Введено некорректное значение!')
        q1 = input('Хотите принять оргтехнику на склад? Да - нажмите 1, Нет - 2: ')
