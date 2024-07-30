import sqlite3
# def insert_vars(dev_id, name, email, join_date, salary):
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print('Connection is OK!!')

#         sqlite_insert = """
#             INSERT INTO sqlitedb_developers
#             (id, name, email, joining_date, salary)
#             VALUES
#             (?, ?, ?, ?, ?);
#             """

#         data_tuple = (dev_id, name, email, join_date, salary)
#         cursor.execute(sqlite_insert, data_tuple)
        
#         sqlite_connection.commit()
#         print("Записи успішно додано")
        
#         cursor.close()

#     except sqlite3.Error as error:
#         print("Помилка підключення до sqlite", error)
#     finally:
#         if (sqlite_connection):
#             sqlite_connection.close()
#             print("З’єднання з SQLite закрите")


# insert_vars(2, "Jane", 'test@gmail.com', '2020-12-12', 5600)
# insert_vars(3, "Jack", 'igo@.com', '2000-12-12', 1115600)


def insert_many_vars(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print('Connection is OK!!')

        sqlite_insert = """
            INSERT INTO sqlitedb_developers
            (id, name, email, joining_date, salary)
            VALUES
            (?, ?, ?, ?, ?);
            """

        cursor.executemany(sqlite_insert, records)
        
        sqlite_connection.commit()
        print("Записи успішно додано")
        
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка підключення до sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("З’єднання з SQLite закрите")

recordsToInsert = [
    (4, "Viktor", 'i@.com', '2019-27-12', 20),
    (5, "Jack", 'isdgdfgdfgo@.com', '2000-12-12', 1600)
]

insert_many_vars(recordsToInsert)