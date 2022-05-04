"""
ТЕСТЫ



"""

import sqlite3

#  СОЗДАЁМ ТАБЛИЦУ ПОЛЬЗОВАТЕЛЕЙ
with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT(50),
        Num TEXT(15))      
    '''
    cursor.execute(query)

#   СОЗДАЕМ ЛОГИКУ СОЗДАНИЯ - ПОИСКА id  в базе данных проверки создан ли пользователь
def User(Username=None, Num=None):
    # входные данные это логин и номер сотового
    try:
        db = sqlite3.connect("database.db")
        cursor = db.cursor()

        cursor.execute("SELECT Num FROM users WHERE Num = ?", [Num])
        if cursor.fetchone() is None:
            values = [Username, Num]

            cursor.execute("INSERT INTO users(Username, Num) VALUES(?, ?)", values)
            db.commit()
            cursor.execute('SELECT id FROM users WHERE Username = ? OR Num = ?',[Username,Num])
            Id = cursor.fetchone()
        else:
            cursor.execute('SELECT id FROM users WHERE Username = ? OR Num = ?',[Username,Num])
            Id = cursor.fetchone()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        return Id
        cursor.close()
        db.close()


#   СОЗДАЕМ ДЛЯ ПОЛЬЗОВАТЕЛЯ ТАБЛИЦУ С ЕГО СООБЩЕНИЯМИ
def UserMessageTable(identifier=15, sms='23445', data='01-02-2020', url=12):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS UsersSms_' + str(
        identifier) + '(id INTEGER PRIMARY KEY AUTOINCREMENT, sms TEXT, data TEXT, url TEXT)')
    db.commit()

    cursor.execute('INSERT INTO UsersSms_' + str(identifier) + '(sms, data, url) VALUES(?, ?, ?)', [sms, data, url])

    db.commit()
    db.close()

#   СОЗДАНИЕ ФУНКЦИИ ВЫВОДА ИНФОРМАЦИИ ПО ID
def message(identifier=1234):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    sql_select_query = "SELECT * FROM UsersSms_"+str(identifier)+""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(record)

id = User('M565656gg4524', 8955934029454)
UserMessageTable(id[0])
message(id[0])
message(2)





if __name__ == "__main__":
    import doctest

    doctest.testmod()
