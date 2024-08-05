import sqlite3


def readTable(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print('Connection is OK!!')

        sql_select_query = """ SELECT * from sqlitedb_developers """
        cursor.execute(sql_select_query)

        records = cursor.fetchall()

        print(f'Всього рядків: {len(records)}')
        print('Вивід усіх рядків: ')

        for row in records:
            print(f'ID: {row[0]}')
            print(f'NAME: {row[1]}')
            print(f'EMAIL: {row[2]}')
            print(f'Joining date: {row[3]}')
            print(f'salary: {row[4]}', end='\n\n')
        
        cursor.close()
    
    except sqlite3.Error as error:
        print("Помилка підключення до sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("З’єднання з SQLite закрите")

readTable(2)