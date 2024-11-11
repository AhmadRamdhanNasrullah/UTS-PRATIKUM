# Program untuk menghitung luas dan keliling persegi panjang

# Meminta input panjang dan lebar dari pengguna
panjang = float(input("Masukkan panjang persegi panjang (dalam satuan meter): "))
lebar = float(input("Masukkan lebar persegi panjang (dalam satuan meter): "))

# Menghitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil perhitungan
print(f"Luas persegi panjang: {luas} meter persegi")
print(f"Keliling persegi panjang: {keliling} meter")
