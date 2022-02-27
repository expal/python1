my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list.insert(1, '"')
my_list.insert(3, '"')
my_list.insert(5, '"')
my_list.insert(7, '"')
my_list.insert(12, '"')
my_list.insert(14, '"')

for num in my_list:
    if num == "5" or num == "+5":
        num = int(num)
        num = str((num // 10)) + str(num)
        my_list[2] = num
        my_list[13] = "+" + num
        x = ' '.join(my_list)
        print(x)
