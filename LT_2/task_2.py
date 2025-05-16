import hashlib

'''
    Створіть функцію generate_file_hashes(*file_paths), яка приймає список шляхів до файлів.
    Для кожного файлу у списку функція повинна:
    Відкрити файл у бінарному режимі для читання.
    Обчислити хеш SHA-256 вмісту файлу.
    Зберегти результати у словнику, де ключем є шлях до файлу,
    а значенням - його SHA-256 хеш (у шістнадцятковому форматі).
    Обробити можливі винятки, такі як відсутність файлу (FileNotFoundError) або
    помилки читання файлу (IOError), виводячи відповідне повідомлення.
    Повернути словник з хешами файлів.
'''

def generate_file_hashes(*file_paths):
    file_hashes = {}

    for path in file_paths:
        try:
            with open(path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hashlib.sha256().update(chunk)
            file_hashes[path] = hashlib.sha256().hexdigest()
        except FileNotFoundError:
            print(f"Файл не знайдено: {path} \n")
        except IOError:
            print(f"Помилка читання файлу: {path}")

    return file_hashes

hashes = generate_file_hashes("./files/1.txt", "./files/2.txt", "./files/3.txt", "./files/4.txt")

for path, h in hashes.items():
    print(f"{path}: {h}")