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

# menghapus list 
store = ['baju', 'celana', 'kemeja', 'kaos']
for i in store:
    print('stock baju {}'. format(i))
print ("=" * 10)

del store[2]
for i in store:
    print('stock toko sekarang {}' . format(i))
    
print ("=" * 10)
store.remove('baju')
for pi in store:
    print('stock tersedia di toko {}' . format(i))

# Memotong list
huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (huruf[1:5])

# penggabungan list
sayuran = ['bayam', 'kangkung', 'kobis']
buah = ['apel', 'sirsak']
jusCampuran = sayuran + buah

print(jusCampuran)
for i in jusCampuran:
    print('macam-macam jus {}' . format(i))

# perkalian list
jusSayur = sayuran * 5
print(jusSayur)


# list multidimensi
list_minuman = [
    ['teh', 'jeruk', 'kopi'],
    ['es teh', 'es jeruk', 'es kopi'],
    ['teh anget', 'jeruk anget', 'kopi anget']
]
print(list_minuman[1][0])
for i in list_minuman:
    print('menu minuman {}' . format(i))
