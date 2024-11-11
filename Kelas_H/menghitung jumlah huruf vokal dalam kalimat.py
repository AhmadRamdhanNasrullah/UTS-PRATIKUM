# Menghitung Jumlah Huruf Vokal dalam Kalimat
kalimat = input("Masukkan kalimat: ")

vokal = 'aeiouAEIOU'
jumlah_vokal = sum(1 for char in kalimat if char in vokal)

print(f"Jumlah huruf vokal: {jumlah_vokal}")
input("#program ini untuk menghitung jumlah huruf vokal didalam kalimat dengan otomatis")
