teman = ['nanang', 'budi', 'bayu', 'cahyo']

print ("ini nama salah satu teman saya {}" . format(teman[2]))
print ("semua teman saya ada {} orang" . format(len(teman)))

for i in teman:
    print("teman saya namanya %s" % i)

teman[2] = "andi"
print ("ini nama salah satu teman saya {}" . format(teman[2]))

for i in teman:
    print("teman saya bernama {}" . format(i))

# menambahkan item ke list
# prepend (menambahkan item dari depan) ~ tidak ada fungsinya
# append (menambahkan item dari belakang)
# insert (menambahkan item sesuai index yang diberikan)
makanan = ['bakso', 'mie', 'gerengan']
makanan.append('cakue')
# makanan.prepend('siomay') ~ tidak bisa digunakan
makanan.insert(2, 'sempol')
print(makanan)