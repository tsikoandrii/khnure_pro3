import hashlib
from datetime import datetime

'''
    Створіть базовий клас User (Користувач) з атрибутами:
    username (ім'я користувача)
    password_hash (хеш пароля)
    is_active (булеве значення, що вказує, чи активований обліковий запис).
    Метод verify_password(password), який приймає пароль та порівнює його з password_hash.
'''

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hashlib.md5(password.encode()).hexdigest()
        self.is_active = False

    def verify_password(self, password):
        hashed = hashlib.md5(password.encode()).hexdigest()

        return self.password_hash == hashed

'''
    Створіть підкласи, що представляють різні ролі користувачів, наприклад:
    
    Administrator (Адміністратор), який успадковує від User та може мати додаткові атрибути або методи, 
    пов'язані з адмініструванням системи (наприклад, список дозволів).
    
    RegularUser (Звичайний користувач), який також успадковує від User та може мати специфічні для 
    звичайних користувачів атрибути (наприклад, остання дата входу).
    
    GuestUser (Гість), який є підкласом User та може мати обмежені права доступу.
'''

class Administrator(User):
    def __init__(self, username, password, permissions):
        super().__init__(username, password)
        self.permissions = permissions

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def has_permission(self, permission):
        return permission in self.permissions

class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None

    def update_last_login(self):
        self.last_login = datetime.now()

class GuestUser(User):
    def __init__(self, username="guest"):
        super().__init__(username, password="guest")

    def has_limited_access(self):
        return True

'''
    Створіть клас AccessControl (Контроль доступу) з атрибутами:
    users (словник, де ключами є імена користувачів, а значеннями - об'єкти класів користувачів).
    Метод add_user(user), який додає нового користувача до системи.
    Метод authenticate_user(username, password), який перевіряє, 
    чи існує користувач з таким ім'ям та чи правильний введений пароль. 
    Повертає об'єкт користувача у разі успішної аутентифікації, і None у разі невдачі.
'''

class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password):
            return user
        return None

# Тестування
admin = Administrator("admin", "adminpass", [])
user = RegularUser("john", "johnpass")
guest = GuestUser()

ac = AccessControl()
ac.add_user(admin)
ac.add_user(user)
ac.add_user(guest)

# Виведе об'єкт або None
s1 = ac.authenticate_user("admin", "adminpass")
print(s1)

s2 = ac.authenticate_user("john", "wrongpass")
print(s2)

# Дефолтний пароль для гостя - guest
s3 = ac.authenticate_user("guest", "guest")
print(s3)