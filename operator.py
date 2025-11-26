# a = int(input('masukkan nilai a: '))
# b = int(input('masukkan nilai b: '))

# Operator Aritmatika
# c = a + b
# print ('hasil %d + %d = %d' % (a,b,c))

# c = a - b
# print ('hasil {} - {} {}' . format(a,b,c))


# Operator Penugasan
# a += 5
# print ("nilai a sekarang {}" .format(a))

# a -= 3
# print ("nilai a sekarang %d" % (a))

# Operator Pembanding
# c = a > b
# print ("hasil perbandingan adalah {}" . format(c))


# Operator Logika
# a = True
# b = False

# c = a & b # and like &
# print ("hasilnya {}" . format(c))
# c = a | b # or like |
# print ("hasilnya {}" . format(c))
# c = not a
# print ("hasilnya {}" . format(c))


# Operator Ternary
umur = int(input('berapa umur anda? '))
aku = "Bocah" if umur < 10 else "Dewasa" # bisa menggunakan ternary ini dengan skema <kondisi true> if <kondisi> else <kondisi false>
aku = ('Bocah', 'Dewasa')[umur < 10] # bisa menggunakan ternary ini dengan skema (<true>, <else>)[<kondisi>]
print (aku)

jomblo = False
status = ('menikah', 'lajang')[jomblo]
print(status)