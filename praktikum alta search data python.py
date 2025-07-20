import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM TBCars
    WHERE id = 101
""")

result = cursor.fetchall()
print(result)

conn.close()