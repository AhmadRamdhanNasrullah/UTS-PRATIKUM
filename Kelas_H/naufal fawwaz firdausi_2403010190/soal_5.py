# Program untuk menampilkan substring berdasarkan indeks awal dan akhir

# Meminta input kata dari pengguna
kata = input("Masukkan sebuah kata: ")

# Meminta input indeks awal dan indeks akhir
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring berdasarkan indeks
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print(f"Substring dari kata '{kata}' antara indeks {indeks_awal} dan {indeks_akhir} adalah: '{substring}'")
