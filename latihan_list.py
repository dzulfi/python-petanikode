hobi = []
stop = False
i = 0

# mengisi hobi
while(not stop):
    hobi_baru = str(input("inputkan hobi anda ke-{}: " . format(i)))
    hobi.append(hobi_baru)

    # Increment i
    i += 1 

    tanya = str(input("Mau isi lagi? (y/t)"))
    if(tanya == 't'):
        stop = True

print ("=" * 10)
print("kamu memiliki {} hobi" . format(len(hobi)))
for x in hobi:
    print ("- {}" . format(x))