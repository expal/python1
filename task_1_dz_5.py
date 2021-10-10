max_num = int(input("Введите число: "))


def odd_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = odd_generator(max_num)
print(next(nums_gen))

