kalimat = str(input("masukan kalimat ="))
vokal = 'aiueoAIUEO'
jumlah_vokal = str(sum(1 for char in kalimat if char in vokal))

print("Jumlah huruf vokal =" +jumlah_vokal)
