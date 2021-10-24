def val_cheker(callback):
    def val_cheker_(func):
        def cheker(x):
            num = func(x)
            if num < 0:
                msg = f'wrong val {num}'
                raise ValueError(msg)
            else:
                print(num)
        return cheker

    return val_cheker_


@val_cheker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(2)
b = calc_cube(-1)