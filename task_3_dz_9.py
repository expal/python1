class Worker:
    name = 0
    surname = 0
    position = 0
    bonus = 0
    _income = 0

    def __init__(self, name, surname, position, bonus, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self.bonus = bonus
        self._income = _income
        self.income_dict = {'income': _income, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self.position}')
        print(f'Итоговый доход: {sum(self.income_dict.values())}')


a = Position('Александр', 'Петров', 'Программист', 50000, 100000)
# print(a.name)
# print(a.surname)
# print(a.position)
# print(a.bonus)
# print(a._income)
# print(a.income_dict)
a.get_full_name()
a.get_total_income()
