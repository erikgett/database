"""
ТЕСТЫ



"""

import sqlite3

#  СОЗДАЁМ ТАБЛИЦУ ПОЛЬЗОВАТЕЛЕЙ



#   СОЗДАЕМ ЛОГИКУ СОЗДАНИЯ - ПОИСКА id  в базе данных проверки создан ли пользователь
def User(message):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,Username TEXT, First_name TEXT,' \
                'Last_name TEXT,User_id TEXT) '
        cursor.execute(query)
    Username=message.from_user.username
    First_name = message.from_user.first_name
    Last_name = message.from_user.last_name
    User_id = message.from_user.id
    try:
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("SELECT User_id FROM users WHERE User_id = ?", [User_id])
        if cursor.fetchone() is None:
            values = [Username, First_name,Last_name,User_id]
            cursor.execute("INSERT INTO users(Username, First_name,Last_name,User_id) VALUES(?, ?, ?, ?)", values)
            db.commit()
    except sqlite3.Error as e:
        print("Error", e)
    finally:

        cursor.close()
        db.close()


#   СОЗДАЕМ ДЛЯ ПОЛЬЗОВАТЕЛЯ ТАБЛИЦУ С ЕГО СООБЩЕНИЯМИ
def UserMessageTable(message,file_id,file_type,message_text):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS UsersSms_' + str(
        message.from_user.id) + '(id INTEGER PRIMARY KEY AUTOINCREMENT, sms TEXT, data TEXT, file_id TEXT, file_type TEXT)')
    db.commit()
    values = [message_text , message.date , file_id , file_type]
    cursor.execute('INSERT INTO UsersSms_' + str(message.from_user.id) + '(sms, data, file_id, file_type) VALUES(?, ?, ?, ?)', values)

    db.commit()
    db.close()


#   СОЗДАНИЕ ФУНКЦИИ ВЫВОДА ИНФОРМАЦИИ ПО ID
def ShowUserMessage(identifier=1234):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    sql_select_query = "SELECT * FROM UsersSms_" + str(identifier) + ""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(record)


def PushUserSmsInDb(message,file_id, file_type,message_text):
    User(message)
    UserMessageTable(message, file_id, file_type,message_text)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
