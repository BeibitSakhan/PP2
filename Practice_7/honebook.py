from connect import connect
import csv

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица готова!")

def insert_console():
    name = input("Name: ")
    phone = input("Phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Контакт '{name}' добавлен!")

def insert_csv():
    conn = connect()
    cur = conn.cursor()
    try:
        with open("contacts.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if len(row) >= 2:
                    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
                    count += 1
        conn.commit()
        print(f"Добавлено {count} контактов из CSV!")
    except FileNotFoundError:
        print("Файл contacts.csv не найден!")
    cur.close()
    conn.close()

def get_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    if not rows:
        print("Таблица пустая!")
    else:
        print(f"\n{'ID':<5} {'Имя':<20} {'Телефон':<15}")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15}")
    cur.close()
    conn.close()

def search_by_name():
    name = input("Search name: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
    rows = cur.fetchall()
    if not rows:
        print("Контакт не найден!")
    else:
        print(f"\n{'ID':<5} {'Имя':<20} {'Телефон':<15}")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15}")
    cur.close()
    conn.close()

def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("New phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    if cur.rowcount == 0:
        print("Контакт не найден!")
    else:
        print(f"Телефон обновлён!")
    cur.close()
    conn.close()

def delete_contact():
    name = input("Enter name to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()
    if cur.rowcount == 0:
        print("Контакт не найден!")
    else:
        print(f"Контакт '{name}' удалён!")
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n1. Add from console")
        print("2. Add from CSV")
        print("3. Show all")
        print("4. Search")
        print("5. Update")
        print("6. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_console()
        elif choice == "2":
            insert_csv()
        elif choice == "3":
            get_all()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT current_database();")
    print("🔌 Подключен к базе:", cur.fetchone()[0])
    cur.close()
    conn.close()
    create_table()
    menu()