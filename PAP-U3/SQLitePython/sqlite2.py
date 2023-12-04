import sqlite3_

sqliteConnection=sqlite3.connect('sql.db')

cursor=sqliteConnection.cursor()

# query='''create table hotels(
# si int primary key,
# name  text,
# location text)'''

# cursor.execute(query)

# query2='''
# insert into hotels values
# (1,'aloft','bellandur'),
# (2,'hilton','whitefield'),
# (3,'marriot','race course rd')
# '''

# cursor.execute(query2)

query3='''
select * from hotels where name like 'A%'
'''

cursor.execute(query3)

result=cursor.fetchall()

for i in result:
    print(i)

# sqliteConnection.commit()
sqliteConnection.close()