import sqlite3


conn = sqlite3.connect('arendа1.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tochkа (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    etazh INTEGER,
    ploshchad REAL,
    konditsioner TEXT,
    stoimost REAL
)
''')
conn.commit()


# ДОБАВИТЬ 10 ЗАПИСЕЙ
def dobavit_10_zapisey():
    dannye = [
        (1, 50.0, 'да', 1000),
        (2, 75.5, 'нет', 1500),
        (1, 30.0, 'да', 800),
        (3, 100.0, 'да', 2500),
        (2, 45.0, 'нет', 900),
        (1, 60.0, 'да', 1200),
        (3, 80.0, 'нет', 1800),
        (2, 55.0, 'да', 1100),
        (1, 40.0, 'нет', 700),
        (3, 90.0, 'да', 2000)
    ]

    cursor.executemany('INSERT INTO tochkа (etazh, ploshchad, konditsioner, stoimost) VALUES (?, ?, ?, ?)', dannye)
    conn.commit()
    print("Добавлено 10 записей")


# ПОКАЗАТЬ ВСЕ ЗАПИСИ
def pokazat_vse():
    cursor.execute('SELECT * FROM tochkа')
    zapisi = cursor.fetchall()
    print("\nВсе записи:")
    print("ID | Этаж | Площадь | Кондиционер | Стоимость")
    print("-" * 50)
    for z in zapisi:
        print(f"{z[0]} | {z[1]} | {z[2]} | {z[3]} | {z[4]}")


# ПОИСК
def poisk():
    print("\nПОИСК:")
    print("1. Поиск по этажу")
    print("2. Поиск по наличию кондиционера")
    print("3. Поиск по стоимости (дешевле указанной)")

    vibor = input("Выберите вариант (1-3): ")

    if vibor == '1':
        etaz = int(input("Введите этаж: "))
        # Запрос 1: поиск по этажу
        cursor.execute('SELECT * FROM tochkа WHERE etazh = ?', (etaz,))

    elif vibor == '2':
        kond = input("Есть кондиционер? (да/нет): ")
        # Запрос 2: поиск по кондиционеру
        cursor.execute('SELECT * FROM tochkа WHERE konditsioner = ?', (kond,))

    elif vibor == '3':
        tsena = float(input("Максимальная стоимость: "))
        # Запрос 3: поиск по стоимости
        cursor.execute('SELECT * FROM tochkа WHERE stoimost < ?', (tsena,))

    else:
        print("Неверный выбор")
        return

    rezultaty = cursor.fetchall()
    if rezultaty:
        print("Найдено:")
        for r in rezultaty:
            print(f"ID: {r[0]}, Этаж: {r[1]}, Площадь: {r[2]}, Кондиционер: {r[3]}, Цена: {r[4]}")
    else:
        print("Ничего не найдено")


# УДАЛЕНИЕ
def udalenie():
    print("\nУДАЛЕНИЕ:")
    print("1. Удалить по ID")
    print("2. Удалить все точки без кондиционера")
    print("3. Удалить точки дороже указанной суммы")

    vibor = input("Выберите вариант (1-3): ")

    if vibor == '1':
        id_tochki = int(input("Введите ID для удаления: "))
        # Запрос 1: удаление по ID
        cursor.execute('DELETE FROM tochkа WHERE id = ?', (id_tochki,))

    elif vibor == '2':
        # Запрос 2: удаление без кондиционера
        cursor.execute('DELETE FROM tochkа WHERE konditsioner = ?', ('нет',))

    elif vibor == '3':
        tsena = float(input("Удалить точки дороже: "))
        # Запрос 3: удаление дорогих точек
        cursor.execute('DELETE FROM tochkа WHERE stoimost > ?', (tsena,))

    else:
        print("Неверный выбор")
        return

    conn.commit()
    print("Удаление выполнено")


# РЕДАКТИРОВАНИЕ
def redaktirovanie():
    print("\nРЕДАКТИРОВАНИЕ:")
    print("1. Изменить стоимость по ID")
    print("2. Добавить кондиционер всем точкам на этаже")
    print("3. Увеличить площадь на 10% для точек с кондиционером")

    vibor = input("Выберите вариант (1-3): ")

    if vibor == '1':
        id_tochki = int(input("Введите ID: "))
        novaya_tsena = float(input("Новая стоимость: "))
        # Запрос 1: изменение стоимости
        cursor.execute('UPDATE tochkа SET stoimost = ? WHERE id = ?', (novaya_tsena, id_tochki))

    elif vibor == '2':
        etazh = int(input("Этаж, где добавить кондиционер: "))
        # Запрос 2: добавление кондиционера на этаже
        cursor.execute('UPDATE tochkа SET konditsioner = ? WHERE etazh = ?', ('да', etazh))

    elif vibor == '3':
        # Запрос 3: увеличение площади на 10%
        cursor.execute('UPDATE tochkа SET ploshchad = ploshchad * 1.1 WHERE konditsioner = ?', ('да',))

    else:
        print("Неверный выбор")
        return

    conn.commit()
    print("Редактирование выполнено")


# МЕНЮ ВЫБОРА ДЕЙСТВИЯ
def main():

    while True:
        print("\n" + "=" * 40)
        print("МЕНЮ:")
        print("1. Добавить 10 записей")
        print("2. Показать все записи")
        print("3. Поиск")
        print("4. Удаление")
        print("5. Редактирование")
        print("6. Выход")

        vibor = input("Выберите действие: ")
        if vibor == '1':
            dobavit_10_zapisey()
        elif vibor == '2':
            pokazat_vse()
        elif vibor == '3':
            poisk()
        elif vibor == '4':
            udalenie()
        elif vibor == '5':
            redaktirovanie()
        elif vibor == '6':
            break
        else:
            print("Неверный выбор")

    conn.close()
    print("Программа завершена")


main()
