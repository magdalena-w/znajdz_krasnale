import sqlite3
#Just to create the .db file

connection = sqlite3.connect("resources/data/krasnale.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE krasnals(x, y, name)")

data = [
    (51.112158, 17.059631, "Babelek Chlaptus"),
    (51.108669,17.065203,"Automatek"),
]

cursor.executemany("INSERT INTO krasnals VALUES(?,?,?)", data)
connection.commit()

for row in cursor.execute("SELECT * FROM krasnals"):
    print(row)

connection.close()