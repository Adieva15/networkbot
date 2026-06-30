import random
import re

# 1. Перемешивание слов
def shuffle_words(text: str) -> str:
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)

# 2. Leetspeak (русско-английский вариант)
LEET_MAP = {
    'а': '@', 'о': '0', 'е': '3', 'и': 'u', 'с': 'c', 'к': 'k', 'р': 'p',
    'т': 't', 'у': 'y', 'х': 'x', 'в': 'b', 'н': 'h', 'л': 'l', 'д': 'd',
    'ё': 'e', 'й': 'u', 'ц': 'c', 'г': 'r', 'ш': 'w', 'щ': 'w', 'з': '3',
    'ъ': 'b', 'ы': 'bI', 'ь': 'b', 'э': 'e', 'ю': 'u', 'я': 'a'
}
def to_leetspeak(text: str) -> str:
    result = []
    for ch in text.lower():
        result.append(LEET_MAP.get(ch, ch))
    return ''.join(result)


# 4. Сравнение двух текстов
def compare_texts(text1: str, text2: str) -> str:
    words1 = set(text1.split())
    words2 = set(text2.split())
    common = words1 & words2
    union = words1 | words2
    if not union:
        return "Оба текста пусты"
    similarity = len(common) / len(union) * 100
    return f"Совпадение слов: {similarity:.1f}%\nОбщих слов: {len(common)}\nВсего уникальных: {len(union)}"

# 5. Транслитерация русский→латиница (простая)
RUS_TO_LAT = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}
def transliterate_ru_to_en(text: str) -> str:
    result = []
    for ch in text.lower():
        result.append(RUS_TO_LAT.get(ch, ch))
    return ''.join(result)
