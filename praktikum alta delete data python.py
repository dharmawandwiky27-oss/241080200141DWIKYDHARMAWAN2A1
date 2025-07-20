import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

# Menghapus data mobil dengan ID 102 dari tabel TBCars
cursor.execute("""
    DELETE FROM TBCars
    WHERE id = 102
""")

# Menyimpan perubahan
conn.commit()

# Menutup koneksi ke database
conn.close()