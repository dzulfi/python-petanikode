makan = []
minum = []
stopFood = False
stopDrink = False
iFood = 0
iDrink = 0

while(not stopFood):
    new_makan = str(input('masukkan makanan anda ke-{}: ' . format(iFood)))
    makan.append(new_makan)

    iFood += 1

    tanya_makan = str(input('Masih mau makan lagi? (y/t)'))
    if(tanya_makan == 't'):
        stopFood = True

print('=' * 10)

while(not stopDrink):
    new_minum = str(input('masukkan minuman anda ke-{}: ' . format(iDrink)))
    minum.append(new_minum)

    iDrink += 1

    tanya_minum = (str(input('Masih mau minum lagi? (y/t)')))
    if (tanya_minum == 't'):
        stopDrink = True

print("^" * 10)
print('kamu memiliki {} makanan' . format(len(makan)))
print('=' * 10)
for i in makan:
    print('pesanan makanan anda {}' . format(i))
    
print("^" * 10)
print('kamu memiliki {} minuman' . format(len(minum)))
print('=' * 10)
for i in minum:
    print('pesanan minuman anda {}' . format(i))