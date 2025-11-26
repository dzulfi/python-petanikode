# Perulangan FOR
ulang = 10
for i in range(ulang):
    print(f"Perulangan ke-{i}")

array = ['kopi', 'teh', 'jus']
for isi in array:
    print(isi)

# Perulangan WHILE
jawab =  'ya'
hitung = 0

while (jawab == 'ya'):
    hitung += 1
    jawab = input("ulang lagi tidak? ")

print(f"total perulangan: {hitung}")