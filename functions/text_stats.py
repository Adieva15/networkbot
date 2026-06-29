import re

def text_stats(text:str)->str:
    if not text:
        return "Текст пуст"
    char_count=len(text)
    char_no_space=len(text.replace(' ', ''))
    word_count=len(text.split())

    return(f"Символов (с пробелами): {char_count}"
           f"Символов (без пробелов): {char_no_space}"
           f"Слов: {word_count}")