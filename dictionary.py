pak_tani = {
    "nama": "Petani Kode",
    "umur": 22,
    "hobi": ["coding", "membaca", "cocok tanam"],
    "menikah": False,
    "sosmed": {
        "facebook": "petanikode",
        "twitter": "@petanikode"
    } 
}

print("nama: {}" . format(pak_tani["nama"]))
print("umur: {}" . format(pak_tani.get("umur")))
# perulangan
print("=" * 10 + " perulangan untuk mengambil dictionary " + "=" * 10)
for i in pak_tani['sosmed']:
    print(f"sosmed pak tani {pak_tani['sosmed'][i]}")
print("=" * 10 + " perulangan untuk mengambil list " + "=" * 10)
for i in pak_tani['hobi']:
    print(f"hobi pak tani {i}")
print("=" * 10)
# perulangan key, value
for key, val in pak_tani.items():
    print("{}: {}" . format(key, val))

# menggunakan konstruktor
warna_buah = dict(jeruk="orange", apel="merah", pisang="kuning")
print(warna_buah["jeruk"])

# mengambil panjang dictionary
length = len(warna_buah)
print(f"jumlah warna buah {length}")
print(f"jumlah data pak tani {len(pak_tani)}")
print(f"jumlah hobi pak tani {len(pak_tani['hobi'])}")
print(f"jumlah sosmed pak tani {len(pak_tani['sosmed'])}")