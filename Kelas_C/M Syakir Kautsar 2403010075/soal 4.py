# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Mendefinisikan huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal dalam kalimat
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

# Menampilkan hasil
print("Jumlah huruf vokal dalam kalimat adalah:", jumlah_vokal)
#irfan nur fadillah akbar
#2403010069