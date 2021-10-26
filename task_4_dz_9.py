from random import choice


class Car:
    speed = 0
    color = 0
    name = 0
    is_police = 0

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина оставновилась')

    def direction(self):
        direction_list = ['налево', 'направо']
        print(f'Машина повернула {choice(direction_list)}')

    def show_speed(self):
        print(f'Скорость машины {self.speed}')

    def police(self):
        if self.is_police is True:
            print('Полицейская')
        else:
            print('Гражданская')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Скорость машины {self.speed}')

    def info_car(self):
        print(f'Машина: {self.name}')
        print(f'Цвет: {self.color}')
        print(f'Скорость: {self.speed}')
        if self.is_police is True:
            print(f'Тип: Полицейская')
        else:
            print(f'Тип: Гражданская')


class SportCar(Car):
    def info_car(self):
        print(f'Машина: {self.name}')
        print(f'Цвет: {self.color}')
        print(f'Скорость: {self.speed}')
        if self.is_police is True:
            print(f'Тип: Полицейская')
        else:
            print(f'Тип: Гражданская')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Скорость машины {self.speed}')

    def info_car(self):
        print(f'Машина: {self.name}')
        print(f'Цвет: {self.color}')
        print(f'Скорость: {self.speed}')
        if self.is_police is True:
            print(f'Тип: Полицейская')
        else:
            print(f'Тип: Гражданская')


class PoliceCar(Car):
    def info_car(self):
        print(f'Машина: {self.name}')
        print(f'Цвет: {self.color}')
        print(f'Скорость: {self.speed}')
        if self.is_police is True:
            print(f'Тип: Полицейская')
        else:
            print(f'Тип: Гражданская')


tc = TownCar(50, 'синий', 'Mazda', False)
tc.info_car()
sc = SportCar(50, 'синий', 'Mazda', False)
sc.info_car()
wc = WorkCar(50, 'синий', 'Mazda', False)
wc.info_car()
pc = PoliceCar(50, 'синий', 'Mazda', True)
pc.info_car()