import random


def jokes(num_jokes):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    jokes_list = []
    while i < num_jokes:
        num_jokes -= 1
        word1 = random.choice(nouns)
        word2 = random.choice(adverbs)
        word3 = random.choice(adjectives)
        joke = f'{word1} {word2} {word3}'
        jokes_list.append(joke)
    print(jokes_list)


jokes(2)
