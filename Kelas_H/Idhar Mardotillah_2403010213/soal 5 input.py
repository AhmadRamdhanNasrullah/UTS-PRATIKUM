# Program untuk mengambil substring berdasarkan indeks awal dan akhir

# Meminta input kata dari pengguna
kata = input("Masukkan sebuah kata: ")

# Meminta input indeks awal dan indeks akhir
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring menggunakan slicing
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print(f"Substring dari indeks {indeks_awal} hingga {indeks_akhir}: {substring}")
