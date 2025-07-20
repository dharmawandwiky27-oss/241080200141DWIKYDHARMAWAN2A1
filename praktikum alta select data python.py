import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM TBCars")

results = cursor.fetchall()
print(results)

conn.close()