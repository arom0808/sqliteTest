import sqlite3, os

if __name__ == "__main__":
    try:
        isInitialized = True
        if not (os.path.exists("sqlite_python.db") and os.path.isfile("sqlite_python.db")):
            isInitialized = False
        sqlite_connection = sqlite3.connect("sqlite_python.db")
        print("База данных создана и успешно подключена к SQLite")
        if not isInitialized:
            cursor = sqlite_connection.cursor()
            cursor.execute("""CREATE TABLE regions (
                                        id integer PRIMARY KEY,
                                        region_name text);""")
            cursor.execute("""CREATE TABLE cities (
                                        id integer PRIMARY KEY,
                                        region_id integer,
                                        city_name text,
                                        FOREIGN KEY (region_id) REFERENCES regions(id));""")
            cursor.execute("""CREATE TABLE users (
                                        id integer PRIMARY KEY,
                                        second_name text,
                                        first_name text,
                                        patronymic text,
                                        region_id integer,
                                        city_id integer,
                                        phone text,
                                        email text,
                                        FOREIGN KEY (region_id) REFERENCES regions(id)),
                                        FOREIGN KEY (city_id) REFERENCES cities(id)));""")
            cursor.execute("""INSERT INTO regions(id,region_name) VALUES(0,\'Краснодарский край\');""")
            record = cursor.execute("""SELECT * FROM regions;""")
            print(record)
        # sqlite_connection.commit()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
