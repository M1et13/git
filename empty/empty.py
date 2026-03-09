import random

WORDS = [
    "кот", "собака", "дом", "лес", "река", "гора", "солнце", "луна", "звезда",
    "машина", "велосипед", "самолет", "поезд", "корабль", "книга", "ручка",
    "тетрадь", "компьютер", "телефон", "планшет", "яблоко", "банан", "апельсин",
    "мандарин", "виноград", "стул", "стол", "кровать", "шкаф", "диван",
    "чашка", "тарелка", "ложка", "вилка", "нож", "зима", "весна", "лето", "осень",
    "утро", "день", "вечер", "ночь", "радость", "грусть", "счастье", "улыбка",
    "дружба", "любовь", "мечта", "игра", "работа", "отдых", "путешествие",
    "город", "деревня", "страна", "мир", "космос", "вода", "огонь", "земля",
    "воздух", "утка", "курица", "петух", "корова", "лошадь", "свинья", "овца",
    "волк", "лиса", "медведь", "заяц", "белка", "ёж", "лось", "олень"
]

points = {
    "comp": 0,
    "player": 0
}


def judge_concatenation(word1, word2, user_answer):
    correct_answer = word1 + word2
    if user_answer == correct_answer:
        return True, "✓ Абсолютно верно! Строки сложены правильно."
    elif user_answer == word1 or user_answer == word2:
        return False, "✗ Ты ввёл только одно слово. Нужно сложить оба!"
    elif user_answer == word1 + " " + word2 or user_answer == word2 + " " + word1:
        return False, "✗ Пробел не нужен! Просто напиши слова подряд."
    elif user_answer == word1.upper() + word2 or user_answer == word1 + word2.upper():
        return False, "✗ Регистр важен! Пиши слова так, как они даны."
    elif len(user_answer) > len(correct_answer) * 2:
        return False, "✗ Твой ответ слишком длинный. Проверь, нет ли лишних символов."
    else:
        return False, f"✗ Неправильно. Правильный ответ: '{correct_answer}'"


while True:
    word1, word2 = random.sample(WORDS, 2)

    print(f"\nСложи строки: '{word1}' + '{word2}'")
    user_input = input("Твой ответ: ")

    is_correct, message = judge_concatenation(word1, word2, user_input)

    if is_correct:
        print(message)
        points["player"] += 1
    else:
        print(message)
        print("Попробуй ещё раз.")
        points["comp"] += 1

    print(f'Счёт: {points["player"]}:{points["comp"]}')
    print("-" * 40)