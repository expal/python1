class Stationery:
    title = 0

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Принадлежность: {self.title}')
        print('Пишу текст')


class Pencil(Stationery):
    def draw(self):
        print(f'Принадлежность: {self.title}')
        print('Рисую')


class Handle(Stationery):
    def draw(self):
        print(f'Принадлежность: {self.title}')
        print('Выделяю')


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()