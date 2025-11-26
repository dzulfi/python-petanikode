harga = int(input('harga beli: '))

bayar = harga

if harga > 1000:
    print('kamu mendapat bonus minama soda')
    print('dan diskon 5%')

    diskon = harga * 100/100
    bayar = harga - diskon

print('total harga beli {}' . format(bayar))