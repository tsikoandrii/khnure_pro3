import sqlite3
import hashlib

# DB setup
db = sqlite3.connect('users.db')
sql = db.cursor()

sql.execute('''
CREATE TABLE IF NOT EXISTS users (
  login TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  full_name TEXT NOT NULL
)
''')
db.commit()

# hash function
def hash(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

# add new user
def createUser():
    login = input("Login: ")
    pw = input("Password: ")
    name = input("Full name: ")
    pw_hash = hash(pw)

    try:
        sql.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
                    (login, pw_hash, name))
        db.commit()
        print("User created.")
    except sqlite3.IntegrityError:
        print("Login already taken.")

# update user password
def updatePw():
    login = input("Login: ")
    new_pw = input("New password: ")
    pw_hash = hash(new_pw)

    sql.execute("UPDATE users SET password = ? WHERE login = ?", (pw_hash, login))
    if sql.rowcount == 0:
        print("User not found.")
    else:
        db.commit()
        print("Password updated.")

# login/auth check
def loginUser():
    login = input("Login: ")
    pw = input("Password: ")
    pw_hash = hash(pw)

    sql.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, pw_hash))
    user = sql.fetchone()

    if user:
        print(f"Welcome, {user[2]}")
    else:
        print("Wrong login or password.")

# main menu
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Create User")
        print("2. Update Password")
        print("3. Login")
        print("4. Exit")

        choice = input("Select option: ")

        match choice:
            case '1': createUser()
            case '2': updatePw()
            case '3': loginUser()
            case '4': break
            case _: print("Invalid option.")

main()
db.close()
