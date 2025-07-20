import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""
    UPDATE TBCars
    SET price = 20000
    WHERE id = 101
""")

print(cursor.fetchall())

conn.commit()
conn.close()