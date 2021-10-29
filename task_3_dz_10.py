class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return Cell(self.quantity - other.quantity)
        else:
            msg = "Разность количества ячеек двух клеток меньше нуля"
            raise ValueError(msg)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __floordiv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, quantity: int):
        rows, tail = self.quantity // quantity, self.quantity % quantity
        return '\n'.join(['*' * quantity] * rows + (['*' * tail] if tail else []))


a = Cell(10)
b = Cell(1231230)
print((a + b).make_order(20))
