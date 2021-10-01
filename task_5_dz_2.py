my_list = [57.8, 46.51, 97, 31.9, 45, 47, 71.4, 76, 12.2, 64]
r = 0
kk = 0
e = 0

for i in my_list:
    x = my_list.index(i)
    if type(i) == float:
        kk = round((i * 10) % 10)
        r = (i * 10) // 10
        kk = str(kk)
        e = str(r) + str(kk)
    elif type(i) == int:
        kk = round((i * 10) % 10)
        r = (i * 10) // 10
        kk = str(kk)
        e = str(r) + kk
    my_list[x] = e
    print(int(r), kk.zfill(2))
    print(my_list)
