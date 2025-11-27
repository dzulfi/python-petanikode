# Perulangan FOR
ulang = 10
for i in range(ulang):
    print(f"Perulangan ke-{i}")

array = ['kopi', 'teh', 'jus']
for isi in array:
    print(isi)

# Perulangan WHILE
jawab =  str('ya')
hitung = 0

# while (jawab == 'ya'):
#     hitung += 1
#     jawab = input("ulang lagi tidak? ")

while (True):
    hitung += 1
    jawab = input("ulangi lagi tidak? ")
    if jawab == 'tidak':
        break

print(f"total perulangan: {hitung}")