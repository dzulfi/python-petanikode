nama = str(input('masukkan nama: '))
umur = int(input('masukkan umur: '))
tinggi = float(input('masukkan tinggi: '))
_tipe = type(nama)

print (tinggi)
print (nama)
print(_tipe)
print ("hallo {} apakabar" . format(nama)) # {} digantikan dengan hasil dari nama

print ("hallo %s, umur %d, tinggi %f" % (nama, umur, tinggi)) # %s for string, %d for desimal, %f for fraction (pecahan)
print ("nama {}, umur {}, tinggi badan {}" . format(nama, umur, tinggi)) # menampilkan output variabel sesuai urutan yang akan dikeluarkan dalam {}