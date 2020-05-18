class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = wage
        self._bonus = bonus
        self._income = {'wage': self._wage, 'bonus': self._bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Фамилия и имя: {self.name} {self.surname}')

    def get_total_income(self):
        z = int(self._income.get('wage')) + int(self._income.get('bonus'))
        print(f'Доход с учетом премии: {z:.2f}')


position_1 = Position('Василий', 'Иванов', 'бухгалтер', 30000, 5000)
print(position_1.name, position_1.surname, position_1.position, position_1._income)
position_1.get_full_name()
position_1.get_total_income()

position_2 = Position('Анна', 'Петрова', 'главный бухгалтер', 60000, 10000)
print(position_2.name, position_2.surname, position_2.position, position_2._income)
position_2.get_full_name()
position_2.get_total_income()
