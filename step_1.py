class OwnError(Exception):
    def __init__(self, txt):
        self.t = txt

my_list = []
w = (input('Введите число для добавления в список. Для выхода введите Q: '))
while True:
    if w != 'Q':
        try:
            if w != float(w):
                raise OwnError('Введено не число!')
        except OwnError as err:
            print(err)
            w = (input('Введите число для добавления в список. Для выхода введите Q: '))
        #except ValueError:
           # print('Введено не число!')
           # w = (input('Введите число для добавления в список. Для выхода введите Q: '))
        else:
            my_list.append(w)
            w = (input('Введите число для добавления в список. Для выхода введите Q: '))
    else:
        print(my_list)
        break




