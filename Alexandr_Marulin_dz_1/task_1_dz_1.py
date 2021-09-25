duration = int(input())

if len(str(duration)) == 2 and duration <= 60:
    print(duration, "сек")
elif len(str(duration)) == 3 or len(str(duration)) == 2 and 61 <= duration <= 99:
    print((duration // 60), "мин", (duration % 60), "сек")
elif len(str(duration)) == 4 or len(str(duration)) == 5 and 10000 <= duration <= 86399:
    print(duration // 3600, "час", ((duration // 60) % 60), "мин", (duration % 60), "сек")
elif len(str(duration)) >= 5:
    print((duration // 86400), "дн", ((duration // 3600) // 100 % 10), "час", ((duration // 60) % 60), "мин", (duration % 60), "сек")
