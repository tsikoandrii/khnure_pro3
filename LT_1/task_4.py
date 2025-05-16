'''
    Система управління задачами.
    Створіть словник, де ключі - це назви задач, а значення - їх статус ("виконано", "в процесі", "очікує").
    Напишіть функції для додавання, видалення та зміни статусу задач.
    Додатково: створіть список задач, які мають статус "очікує".
'''

tasks = {
    "Розробити енд-поінт для смс-верифікації користувача": "pending",
    "Розробити UI-компонент (PasswordInput)": "in progress",
    "Написати unit-тести для форми входу": "pending",
    "Оновити README.md у репозиторії": "done",
    "Задеплоїти додаток на staging-сервер": "in progress",
    "Створити міграцію для нової таблиці users_log": "pending",
    "Оптимізувати SQL-запити для dashboard": "in progress"
}

def add_task(name, status):
    tasks[name] = status

def remove_task(name):
    if name in tasks:
        del tasks[name]
    else:
        print(f"Задача '{name}' не знайдена.")

def update_status(name, status):
    if name in tasks:
        tasks[name] = status
    else:
        print(f"Задача '{name}' не знайдена. Неможливо оновити статус.")

def get_tasks_by_status(status):
    result = []

    for task in tasks:
        if tasks[task] == status:
            result.append(task)

    return result

# --- Тестові виклики --- #
add_task("Провести код-рев'ю для pull request #42", "pending")
update_status("Розробити UI-компонент (PasswordInput)", "done")
remove_task("Оновити README.md у репозиторії")

pending_tasks = get_tasks_by_status("pending")

print("Задачі зі статусом 'очікує':")
for t in pending_tasks:
    print("-", t)

print("\nУсі задачі зі статусами:")
for task, status in tasks.items():
    print(f"- {task}: {status}")