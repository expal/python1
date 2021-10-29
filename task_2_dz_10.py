from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return round(self.param / 6.5 + 0.5) + round(2 * other.param + 0.3)


class Coat(Clothes):

    @property
    def calc(self):
        return f'Пальто {round(self.param / 6.5 + 0.5)}'


class Suit(Clothes):

    @property
    def calc(self):
        return f'Костюм {round(2 * self.param + 0.3)}'


a = Suit(10)
b = Coat(20)
print(a + b)
