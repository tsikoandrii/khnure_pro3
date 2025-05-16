'''
    Напишіть функцію filter_ips(input_file_path, output_file_path, allowed_ips),
    яка аналізує IP-адреси з лог-файла http-сервера:
    Читає IP-адреси з кожного рядка файлу input_file_path.
    Перевіряє, чи кожна прочитана IP-адреса присутня у списку дозволених IP-адрес allowed_ips.
    Попередньо необхідно задати список (масив) дозволених IP-адрес allowed_ips.
    Рахує скільки разів зустрічаються дозволені адреси у лог файлі.
    Записує результат аналізу лог-файлу до файлу output_file_path,
    у вигляді <IP адерса> - <кількість входженнь>.
    Обробити можливі винятки, такі як відсутність вхідного файлу (FileNotFoundError) або
    помилки запису до вихідного файлу (IOError), виводячи інформативні повідомлення.
'''

ALLOWED = (
    '110.136.166.128',
    '50.150.204.184',
    '66.249.73.135',
    '218.30.103.62',
    '86.1.76.62',
    '208.115.111.72'
)

def filter_ips(log_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(log_file_path, 'r', encoding='utf-8') as logs:
            for line in logs:
                ip = line.strip().split("-")[0].strip()

                if ip in allowed_ips:
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1

        return ip_counts

    except FileNotFoundError:
        print(f"Помилка: файл '{log_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{log_file_path}'.")
    return None

filtered = filter_ips('./apache_logs.txt', ALLOWED)

print(filtered)