def generator():
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', "Станислав", "Катя"]
    g_tutor = (tutor for tutor in tutors)
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    g_klass = (klass for klass in klasses)
    for i in range(len(tutors)):
        print((next(g_tutor), next(g_klass)))


generator()

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [el for el in src if src[el] < src[el + 1]]
# print(result)
