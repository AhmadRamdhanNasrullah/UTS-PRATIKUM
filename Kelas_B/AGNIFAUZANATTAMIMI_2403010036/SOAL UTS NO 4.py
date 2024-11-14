kalimat = input("masukan kalinmat")
huruf_vokal = "A,I,U,E,O,a,i,u,e,o"
jumlah_vokal = sum(1 for huruf in kalimar if huruf in huruf_vokal)
print("jumlah huruf vokal",jumlah_vokal)
