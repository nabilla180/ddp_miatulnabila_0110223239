# no. 1
import math
kendaraan = ["B 5678 CD", "Honda CBR600", 600, "Hitam"]

# no. 2
kendaraan.append("Rp. 45,320,000")
kendaraan.append(2)
kendaraan.insert(2, "Honda")
kendaraan. insert(3, "Re very Mat Red")

print(kendaraan)

# no 3


def hitung_luas(bentuk, *args):
    match bentuk:
        case "persegi":
            sisi = args[0]
            luas_persegi = sisi ** 2
            return luas_persegi
        case "lingkaran":
            jari_jari = args[0]
            luas_lingkaran = math.pi * jari_jari ** 2
            return luas_lingkaran
        case "segitiga":
            alas, tinggi = args[0], args[1]
            luas_segitiga = 0.5 * alas * tinggi
            return luas_segitiga
        case _:
            return " Salah masukkan pilihan"
