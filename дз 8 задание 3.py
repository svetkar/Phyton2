class OwnError(Exception):
    def __init__(self, txt):
        self.t = txt


my_list = []
w = (input('Введите число для добавления в список. Для выхода введите Q: '))
while True:
    if w != 'Q':
        try:
            if w.isdigit():
                w != float(w)
                my_list.append(w)
            else:
                raise OwnError('Введено не число!')
        except OwnError as err:
            print(err)
            w = (input('Введите число для добавления в список. Для выхода введите Q: '))

        else:
            w = (input('Введите число для добавления в список. Для выхода введите Q: '))
    else:
        print(my_list)
        break
