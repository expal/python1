def thesaurus(*names):
    name_dict = {}
    for name in names:
        first_letter = name[0].title()
        if first_letter not in name_dict:
            name_dict[first_letter] = []
        name_dict[first_letter].append(name)
        print(name_dict)


thesaurus('Вася', 'Петя', "птеры")
