# Program untuk menghitung jumlah huruf vokal dalam kalimat

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Mendefinisikan huruf vokal
vokal = "aeiouAEIOU"

# Inisialisasi penghitung vokal
jumlah_vokal = 0

# Menghitung jumlah huruf vokal dalam kalimat
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print(f"Jumlah huruf vokal dalam kalimat adalah: {jumlah_vokal}")
