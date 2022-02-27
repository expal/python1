my_list = []
x = 0

for i in range(1, 1001, 2):
    x = i ** 3
    my_list.append(x)

if ((x // 1000) + ((x // 100) % 10) + ((x % 10) % 10) + ((x // 10) % 10)) // 7:
    x += x
    print(x)
for i in range(len(my_list)):
    my_list[i] = my_list[i] + 17
if ((x // 1000) + ((x // 100) % 10) + ((x % 10) % 10) + ((x // 10) % 10)) // 7:
    x += x
    print(x)