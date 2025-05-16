'''
    Робота з текстом.
    Напишіть функцію, яка приймає рядок як вхідні дані та повертає словник,
    де ключі - це унікальні слова в рядку, а значення - кількість їх появ.
    Створіть та виведіть на екран список, де зберігаються слова, що зустрічаються більше 3 разів.
'''

def word_count(text):
    words = text.split()
    counts = {}

    for word in words:
        word = word.strip('.,!?').lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

text = """
    приклад тексту текст текст текст і ще трохи тексту
    багато багацько тексту багато багато багато звуків
"""

counts = word_count(text)
freq_words = [word for word, count in counts.items() if count > 3]

print("Словник:", counts)
print("Слова, що зустрічаються більше 3 разів:", freq_words)
