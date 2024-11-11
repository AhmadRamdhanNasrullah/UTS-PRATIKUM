# Program untuk menghitung jumlah huruf vokal dalam kalimat

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal yang akan dihitung
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal dalam kalimat
jumlah_vokal = sum(1 for char in kalimat if char in vokal)

# Menampilkan hasil jumlah huruf vokal
print(f"Jumlah huruf vokal dalam kalimat: {jumlah_vokal}")
