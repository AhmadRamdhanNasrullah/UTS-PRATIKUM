# Menghitung Jumlah Huruf Vokal dalam Kalimat
kalimat = input("Masukkan kalimat: ")

vokal = 'aeiouAEIOU'
jumlah_vokal = sum(1 for char in kalimat if char in vokal)

print(f"Jumlah huruf vokal: {jumlah_vokal}")
# Keterangan
# Ini adalah cara memsukan kalimat dengan cara for,in,if,in dan jumlah huruf vokal dengan codingan
# Nama: Muhammad Alif Al-Asyarie
# NIM: 2403010189
