import sqlite3_

sqliteConnection =sqlite3.connect('sql.db')

cursor=sqliteConnection.cursor()
print('DB Init')

query='select sqlite_version()'

cursor.execute(query)

result=cursor.fetchall()

print('SQLite version is {}'.format(result))

cursor.close()