class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки авторучкой.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером.')


pen_1 = Pen('Pen S')
print(pen_1.title)
pen_1.draw()
pencil_1 = Pencil('Pencil M')
print(pencil_1.title)
pencil_1.draw()
handle_1 = Handle('Handle N')
print(handle_1.title)
handle_1.draw()
