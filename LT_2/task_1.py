'''
    Напишіть функцію analyze_log_file(log_file_path),
    яка приймає шлях до файлу журналу http-сервера (текстового файлу). Функція повинна:

    Прочитати кожний рядок файлу. Типовий лог-файл “apache_logs.txt” додається
    Визначити кількість входжень унікальний кодів відповідей http-сервера (наприклад, 200, 404, 500 і т.д.).
    Зберегти результати у словнику, де ключем є код відповіді, а значенням - кількість його входжень.
    Обробити можливі винятки, такі як відсутність файлу (FileNotFoundError)
    або помилки читання файлу (IOError), виводячи інформативне повідомлення про помилку.

    Повернути отриманий словник з результатами аналізу.
'''
def analyze_log_file(log_file_path):
    status_counts = {}

    try:
        with open(log_file_path, 'r', encoding='utf-8') as logs:
            for line in logs:
                parts = line.split('"')
                if len(parts) > 2:
                    status = parts[2].strip().split()[0]
                    status_counts[status] = status_counts.get(status, 0) + 1
        return status_counts

    except FileNotFoundError:
        print(f"Помилка: файл '{log_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{log_file_path}'.")
    return None

counts = analyze_log_file('./apache_logs.txt')

print(counts)