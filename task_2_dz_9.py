class InputData:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class Road(InputData):
    def calc_road(self):
        print(f'{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) // 1000} т.')


r = Road(20, 5000)
r.calc_road()
