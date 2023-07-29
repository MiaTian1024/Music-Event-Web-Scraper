import sqlite3

# establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# query data
cursor.execute("SELECT * FROM events WHERE date='2022.02.02'")
rows = cursor.fetchall()
print(rows)


# insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.10'),
            ('Hens', 'Hen City', '2088.09.09')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events WHERE band='Cats'")
rows = cursor.fetchall()
print(rows)
