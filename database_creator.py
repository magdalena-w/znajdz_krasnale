import csv, sqlite3

conn = sqlite3.connect( "resources/data/krasnale.db" )
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS krasnals (x, y, name, address, author, localization)')

reader = csv.reader(open('resources/data/krasnal_db.csv', 'r'), delimiter=';')
for field1, field2, field3, field4, field5, field6 in reader:
    cur.execute('INSERT INTO krasnals (x, y, name, address, author, localization) VALUES (?,?,?,?,?,?)', (field1, field2, field3, field4, field5, field6))
#data = cur.fetchall()

for row in cur.execute("SELECT * FROM krasnals"):
    print(row)
    
conn.commit()
conn.close()    
        
        
#cursor.execute("CREATE TABLE krasnals(x, y, name, address, author, localization)")
#
#    csv_data = csv.reader(open("resources/data/krasnal_db.csv"), delimiter=";")
#    for rows in csv_data: # Iterate through csv
#        cursor.execute("INSERT INTO krasnals(x, y, name, address, author, localization) VALUES (?,?,?,?,?)", *rows)
#
#data = [
#    (51.112158, 17.059631, "Babelek Chlaptus"),
#    (51.108669,17.065203,"Automatek"),
#]
#
#cursor.executemany("INSERT INTO krasnals VALUES(?,?,?)", data)
#connection.commit()
#
#for row in cursor.execute("SELECT * FROM krasnals"):
#    print(row)
#
#connection.close()