class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = list(matrix_list)

    def __str__(self):
        return '\n'.join(str(el) for el in self.matrix_list)

    def __add__(self, other):
        result = []

        for item in zip(self.matrix_list, other.matrix_list):
            result.append([sum([el, num]) for el, num in zip(*item)])

        return Matrix(result)


m = Matrix([[31, 32], [37, 43], [51, 86]])
m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(m + m1)
