'''
    Аутентифікація користувачів.
    Створіть словник в якому зберігаються ім'я користувача(login), зашифрований пароль та повне ПІБ користувача.
    Для хешування пароля використовуйте функцію hashlib.md5().
    Зробіть функцію перевірки введеного паролю користувача;
    пароль користувач вводить з консолі, зчитування за допомогою методу input()
'''

import hashlib

users = {
    "ivan123": {
        "password": hashlib.md5("Nv4V4CwxC@".encode()).hexdigest(),
        "full_name": "Іваненко Іван Іванович"
    },
    "olena456": {
        "password": hashlib.md5("MD%87=czvG".encode()).hexdigest(),
        "full_name": "Ковальчук Олена Василівна"
    },
    "admin": {
        "password": hashlib.md5("123765".encode()).hexdigest(),
        "full_name": "Content Administrator"
    },
    "root": {
        "password": hashlib.md5("root".encode()).hexdigest(),
        "full_name": "Root User"
    }
}

def authenticate(login):
    if login not in users:
        print("Користувача не знайдено")
        return

    password_input = input("Введіть пароль: ")
    hashed_input = hashlib.md5(password_input.encode()).hexdigest()

    if hashed_input == users[login]["password"]:
        print(f"Успішна авторизація! Вітаємо, {users[login]['full_name']}")
    else:
        print("Невірний пароль")

user_login = input("Введіть логін: ")
authenticate(user_login)
