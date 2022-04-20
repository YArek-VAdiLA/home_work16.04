import sqlite3

def selectday(day):
    try:

        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM WeekDat WHERE  d = ?;"
        cursor.execute(sqlite_select_query, (day,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")



