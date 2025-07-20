# 241080200141DWIKYDHARMAWAN2A1
Repository ini berisi hasil praktikum UAS mata kuliah Algoritma dan Struktur Data (ALTA) yang berfokus pada pengelolaan database menggunakan SQLite3 dan bahasa pemrograman Python.
Seluruh kode ditulis dan dijalankan secara modular (terpisah per file) untuk menunjukkan pemahaman terhadap operasi CRUD (Create, Read, Update, Delete) dan Search.

Database yang digunakan: cars.db
Tabel utama: TBCars

#Urutan Eksekusi Normal:

CreateTable.py = buat tabel dengan menjalankannya cukup sekali saja.
InsertData.py = menambahkan isi data dari isi tabel.
SelectData.py = untuk memverifikasi data yang sudah masuk.
UpdateData.py = untuk mengubah data berdasarkan ID.
SelectData.py = untuk mengecek hasil perubahan (update).
DeleteData.py = untuk menghapus data berdasarkan ID.
SelectData.py = untuk melihat hasil setelah penghapusan.
SearchData.py = untuk mencari data tertentu berdasarkan ID.
#Urutan Eksekusi Versi Tambahan:

CreateTable.py = buat tabel dengan menjalankannya cukup sekali saja (jika sudah membuat dengan cara sebelumnya, maka biarkan saja dan langsung lanjut langkah kedua).
InsertData.py = menambahkan isi data dari isi tabel.
SelectData.py = untuk memverifikasi data yang sudah masuk.
UpdateData.py = untuk mengubah data berdasarkan ID.
SelectData.py = untuk mengecek hasil perubahan (update).
InsertData1.py = karena saya ingin membuat ulang datanya dan menambahkan beberapa isi datanya seperti ID 102 dan ID 103.
Selectdata.py = untuk mengecek hasil data baru yang sudah masuk.
DeleteData.py = untuk menghapus data berdasarkan ID (disini saya ingin menghapus ID 102), namun tanpa print hasilnya diterminal sehingga harus cek kembali ke SelectData.py.
SelectData.py = untuk melihat hasil setelah pengahapusan ID 102.
DeleteData1.py = untuk menghapus data berdasarkan ID (ID 103), namun pada kode ini akan menampilkan hasilnya diterminal dengan memasukan select * from pada kolom editor dan print(k.fetchall()).
InsertData1.py = insert lagi dengan menghapus kembali semua data pada tabel TBCars dan membuat ulang isi datanya.
SearchData.py = untuk mencari data tertentu berdasarkan ID (disini saya ingin mencari isi data yang diwakili oleh ID 101).
SearchData1.py = untuk mencari data tertentu berdasarkan ID (disini saya ingin mencari isi data yang diwakili oleh ID 102).
Seluruh file pada repository ini merupakan hasil dari Praktikum UAS PBL02 yang mengimplementasikan operasi database menggunakan SQLite3 dan Python. Semua script telah diuji dan berjalan dengan baik secara terpisah sesuai fungsi masing-masing. Diharapkan repository ini dapat menjadi referensi dalam memahami dasar pengelolaan database menggunakan Python.

Terima kasih.
