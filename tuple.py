# Penulisan tuple
t = 123, 321, "asd"
k = (123, 321, "asd")
kosong = () # tuple kosongan

tuple = (['list 1', 'list 2'], {1,2,3}, True)

print(tuple)
print(k[1])


# Netsted Tuple (tuple diisi dengan tuple)
netsted = t, k
print(netsted)


# Sequence Unpacking (mengekstrak tuple)
web = 123, "Petani Kode", "https://www.petanikode.com"
# lalu di-unpacking
id_web, nama, url = web

print(id_web)
print(nama)
print(url)