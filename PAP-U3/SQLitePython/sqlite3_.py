import sqlite3

sqliteConnection=sqlite3.connect('sql.db')

cursor=sqliteConnection.cursor()

query='''
select * from hotels
'''

query1='''
select * from hotels order by name desc limit 1
'''

query2='''
delete from hotels where si>2
'''

cursor.execute(query2)
cursor.execute(query)

result=cursor.fetchall()

print(result)

sqliteConnection.close()