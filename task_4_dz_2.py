my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in my_list:
    x = ' '.join(my_list)
    e = x.split(' ')
    for name in e:
        if name == "Игорь" or name == "МАРИНА" or name == "нИКОЛАй" or name == "аэлита":
            name = name.title()
            print("Привет, " + name)
    break
