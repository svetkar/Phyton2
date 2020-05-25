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


sklad_1 = Sklad({'printer': 10, 'scanner': 15, 'xerox': 5})
print(sklad_1)
otdely = {1: {'printer': 1, 'scanner': 2, 'xerox': 1}, 2: {'printer': 1, 'scanner': 1, 'xerox': 2}}
print(f'Запасы в отделах: {otdely}')
q1 = input('Хотите принять оргтехнику на склад? Да - нажмите 1, Нет - 2: ')
while True:
    if q1 == 1:
        q2 = input('Какую оргтехнику хотите принять на склад: принтер - 1, сканер - 2, ксерокс - 3: ')
        try:
            if q2 == 1 or q2 == 2 or q2 == 3:
                q3 = input('Введите количество: ')
                try:
                    q3 = int(q3)
                    if q2 == 1:
                        q2 = 'printer'
                    if q2 == 2:
                        q2 = 'scanner'
                    else:
                        q2 = 'xerox'
                    sklad_1.priem(q2, q3)
                except ValueError:
                    print('Введено не число!')
                q3 = input('Введите количество: ')
            else:
                print('Выбран неверный пункт.')
                q2 = input('Какую оргтехнику хотите принять на склад: принтер - 1, сканер - 2, ксерокс - 3: ')
    if q1 == 2:
        print('Переход в другое меню.')
    else:
        print('Введено некорректное значение. ')
q1 = input('Хотите принять оргтехнику на склад? Да - нажмите 1, Нет - 2: ')

# sklad_1.priem('printer', 2)
# print(f'На склад поступили 2 новых принтера: {sklad_1}')
# sklad_1.peremeschenie('scanner', 1, 1, otdely)
# print('Со склада в отдел 1 перемещен 1 сканер')
# print(sklad_1)
# print(f'Запасы в отделах: {otdely}')
# sklad_1.spisanie('xerox', 3)
# print('Со склада списаны 3 ксерокса.')
# print(sklad_1)
