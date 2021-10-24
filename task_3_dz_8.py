def logger(func):
    def type_logger(*args, **kwargs):
        for kwarg in kwargs:
            print(f'{kwarg}: {type(kwarg)}')
        for arg in args:
            print(f'{arg}: {type(arg)}')

    return type_logger


@logger
def calc_cube(*args):
    return args


calc_cube(5, 5.1, "abc")

