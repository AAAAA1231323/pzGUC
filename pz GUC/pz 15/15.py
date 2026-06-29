#Приложение БАНК для отслеживания накапливаемых на счетах клиентов банка
#сумм. Таблица Клиент должна содержать следующую информацию: Код клиента, Клиент
#(Ф.И.О.), Периодический платеж, Годовой %, Срок вклада, Пластиковая карта
#(логическое поле), Конечная сумма.



import sqlite3


def init_db():
    """Создание базы данных и заполнение 10 стартовыми позициями."""
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Client (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT NOT NULL,
        payment REAL,
        percent REAL,
        term INTEGER,
        has_card INTEGER,
        total_amount REAL
    )
    ''')

    cursor.execute("DELETE FROM Client")

    initial_clients = [
        ("Иванов Иван Иванович", 5000.0, 12.5, 12, 1, 150000.0),
        ("Петров Петр Петрович", 10000.0, 14.0, 24, 0, 340000.0),
        ("Сидоров Сидор Сидорович", 0.0, 11.0, 6, 1, 45000.0),
        ("Кузнецов Алексей Владимирович", 15000.0, 15.0, 36, 1, 720000.0),
        ("Попова Елена Николаевна", 2000.0, 9.5, 12, 0, 35000.0),
        ("Смирнов Дмитрий Александрович", 7000.0, 13.0, 18, 1, 185000.0),
        ("Васильев Константин Сергеевич", 25000.0, 16.0, 48, 1, 1500000.0),
        ("Федоров Михаил Юрьевич", 0.0, 10.5, 12, 0, 95000.0),
        ("Соколов Олег Игоревич", 12000.0, 13.5, 24, 1, 410000.0),
        ("Морозова Анна Дмитриевна", 4000.0, 11.5, 6, 0, 58000.0)
    ]

    cursor.executemany('''
    INSERT INTO Client (fio, payment, percent, term, has_card, total_amount)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', initial_clients)

    conn.commit()
    print(" База данных успешно инициализирована. Внесено 10 позиций.")
    conn.close()


def print_table(title, rows):
    print(f"\n--- {title} ---")
    print(f"{'ID':<4} | {'Ф.И.О.':<30} | {'Платеж':<8} | {'%':<5} | {'Срок':<5} | {'Карта':<5} | {'Итог':<10}")
    print("-" * 85)
    for r in rows:
        print(f"{r[0]:<4} | {r[1]:<30} | {r[2]:<8} | {r[3]:<5} | {r[4]:<5} | {r[5]:<5} | {r[6]:<10}")


def execute_searches():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Client WHERE total_amount > 300000")
    print_table("Запрос 1 (Поиск): Конечная сумма > 300 000 руб.", cursor.fetchall())

    cursor.execute("SELECT * FROM Client WHERE has_card = 1 AND term = 12")
    print_table("Запрос 2 (Поиск): Есть карта И срок равен 12 мес.", cursor.fetchall())

    cursor.execute("SELECT * FROM Client WHERE fio LIKE 'Сид%' OR fio LIKE 'Куз%'")
    print_table("Запрос 3 (Поиск): Фамилия начинается на Сид% или Куз%", cursor.fetchall())

    conn.close()


def execute_updates():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    print("\n[Редактирование данных...]")

    cursor.execute("UPDATE Client SET percent = percent + 1.5 WHERE term >= 24")
    print(f"Запрос 1 (Изменение): Изменен годовой % для долгосрочных вкладов. Затронуто строк: {cursor.rowcount}")

    cursor.execute("UPDATE Client SET payment = 0.0 WHERE total_amount > 1000000")
    print(f"Запрос 2 (Изменение): Обнулен платеж для миллионеров. Затронуто строк: {cursor.rowcount}")

    cursor.execute("UPDATE Client SET has_card = 1 WHERE id = 2")
    print(f"Запрос 3 (Изменение): Выдана карта клиенту с ID = 2. Затронуто строк: {cursor.rowcount}")

    conn.commit()
    conn.close()


def execute_deletes():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    print("\n[Удаление данных...]")

    cursor.execute("DELETE FROM Client WHERE payment = 0.0 AND total_amount < 50000")
    print(f"Запрос 1 (Удаление): Удалены неактивные мелкие вклады. Затронуто строк: {cursor.rowcount}")

    cursor.execute("DELETE FROM Client WHERE term = 6")
    print(f"Запрос 2 (Удаление): Удалены краткосрочные вклады (6 мес). Затронуто строк: {cursor.rowcount}")

    cursor.execute("DELETE FROM Client WHERE id = 5")
    print(f"Запрос 3 (Удаление): Удален клиент с ID = 5. Затронуто строк: {cursor.rowcount}")

    conn.commit()

    cursor.execute("SELECT * FROM Client")
    print_table("Финальное состояние таблицы после всех удалений", cursor.fetchall())

    conn.close()


if __name__=="__main__":
    init_db()
    execute_searches()
    execute_updates()
    execute_deletes()