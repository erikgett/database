import sqlite3




with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        number TEXT);
    CREATE TABLE IF NOT EXISTS usermessage(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        time TEXT)         
    '''
    cursor.executescript(query)




def NewUser(Username = 'erik' , Num = '89945230'):
    try:
        db = db = sqlite3.connect('database.db')
        db.cursor()
    except:
        pass
#
#     try:
#         db = sqlite3.connect('database.db')
#         cursor = db.cursor()
#         cursor.execute('SELECT username FROM users WHERE username = ?', [Username])
#         if cursor.fetchone() is None:
#             cursor.execute('INSERT INTO users(username ,number)')
#             cursor.execute("INSERT INTO users(username, number) VALUES (?, ?)", values)
#             db.commit()
#         else:
#             print('Логин существует!')
#             NewUser()
#     except sqlite3.Error as e:
#         print('Error', e)
#     finally:
#         cursor.close()
#         db.close()

# NewUser('feri2','89767967')
# NewUser('vfuf','89767967')
# NewUser('erik','89767967')







    # cursor.execute('SELECT * FROM users')
    # print(cursor.fetchall())
    #
    # for user in cursor.execute('SELECT username FROM users'):
    #     print(user)

