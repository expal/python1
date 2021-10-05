def num_translate_adv(num):
    num_dict = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    for key, value in num_dict.items():
        num1 = num.lower()
        if key == num1 and num.istitle():
            print(value.capitalize())
        elif key == num1 and num.islower():
            print(value.lower())
        elif num1 not in num_dict:
            print(None)
            break


num_translate_adv("Eight")
