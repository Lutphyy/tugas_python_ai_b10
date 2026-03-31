# bagian variabel
nama = "Luthfi"
umur = 20
tinggi = 170.5
mahasiswa = True
hobi = ["ngoding", "game", "ngopi", "nonton", "jalan"]

print("Data awal:")
print(nama, umur, tinggi, mahasiswa, hobi)


# main-main string
print("\n--- String ---")
kata1 = "halo"
kata2 = "dunia"

gabung = kata1 + " " + kata2
print("hasil gabung:", gabung)
print("panjang:", len(gabung))
print("besar:", gabung.upper())
print("kecil:", gabung.lower())


# hitung-hitungan
print("\n--- Matematika ---")
a = 10
b = 3

print("tambah:", a + b)
print("kurang:", a - b)
print("kali:", a * b)
print("bagi:", a / b)
print("bagi bulat:", a // b)
print("sisa:", a % b)


# list
print("\n--- List ---")
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

print("isi awal:", buah)
print("ambil satu:", buah[2])

buah.append("melon")
print("tambah item:", buah)

buah.pop(1)
print("hapus satu:", buah)


# input user
print("\n--- Input ---")
nama_user = input("nama kamu: ")
umur_user = input("umur kamu: ")

print("halo, nama saya", nama_user, "umur", umur_user, "tahun")