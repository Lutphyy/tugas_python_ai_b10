# ======================
# LIST
# ======================
data = ["apel", 10, "jeruk", 25, "mangga", 50]

print("List awal:", data)
print("Pertama:", data[0])
print("Terakhir:", data[-1])
print("Slicing [1:5:2]:", data[1:5:2])

# sebelum manipulasi
print("\nSebelum:", data)

data.append("pisang")
data.insert(1, "anggur")
data.extend([100, "melon"])
data.pop()
data.remove("jeruk")

# sesudah manipulasi
print("Sesudah:", data)


# ======================
# TUPLE
# ======================
tup = ("Luthfi", 20, "Informatika", "Batam", "Indonesia")

print("\nTuple:", tup)
print("Panjang:", len(tup))
print("Index ke-2:", tup[2])

# unpacking
nama, umur, *rest = tup
print("Nama:", nama)
print("Umur:", umur)
print("Sisa:", rest)


# ======================
# SET
# ======================
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet1:", set1)
print("Set2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# duplikat hilang
duplikat = {1, 1, 2, 2, 3, 3}
print("Set tanpa duplikat:", duplikat)


# ======================
# DICTIONARY
# ======================
mhs = {
    "nama": "Luthfi",
    "nim": "123456",
    "angkatan": 2023,
    "kota": "Batam"
}

print("\nData awal:", mhs)

# tambah
mhs["jurusan"] = "Informatika"

# ubah
mhs["kota"] = "Tanjungpinang"

# hapus
mhs.pop("angkatan")

print("Setelah update:", mhs)

print("Keys:", mhs.keys())
print("Values:", mhs.values())
print("Items:", mhs.items())

print("\nIterasi:")
for k, v in mhs.items():
    print(k, ":", v)


# ======================
# NESTED STRUCTURE
# ======================
buku = [
    {"judul": "Python Dasar", "penulis": "A", "tahun": 2020},
    {"judul": "Belajar Web", "penulis": "B", "tahun": 2022},
    {"judul": "AI Modern", "penulis": "C", "tahun": 2023},
    {"judul": "Data Science", "penulis": "D", "tahun": 2019}
]

print("\nDaftar judul:")
for b in buku:
    print("-", b["judul"])

# filter
hasil = [b for b in buku if b["tahun"] >= 2021]
print("\nBuku >= 2021:", hasil)


# ======================
# COMPREHENSION
# ======================
angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("\nGenap:", genap)
print("Kuadrat:", kuadrat)

# dict comprehension
mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Mapping:", mapping)

# set comprehension
kalimat = "Belajar Python Itu Seru"
huruf = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf)


# ======================
# KEANGGOTAAN
# ======================
print("\nCek data:")

if "apel" in data:
    print("apel ada di list, index:", data.index("apel"))
else:
    print("apel tidak ada")

if 3 in set1:
    print("3 ada di set")
else:
    print("3 tidak ada")