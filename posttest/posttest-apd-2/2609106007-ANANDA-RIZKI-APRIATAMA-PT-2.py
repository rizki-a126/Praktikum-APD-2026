barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

total_barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]

total_harga = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
total_pajak = total_harga * 0.15
total_bayar = total_harga + total_pajak

rata_rata = total_bayar / len(total_barang)

nim = 7
bolean = nim < rata_rata

total_ringgit = total_bayar / 4360

total_franc_swiss = total_bayar / 21665.05

barang_ganjil = total_barang[0:5:2]

print("Barang 1: Rp", barang_1)
print("Barang 2: Rp", barang_2)
print("Barang 3: Rp", barang_3)
print("Barang 4: Rp", barang_4)
print("Barang 5: Rp", barang_5)
print("Barang 6: Rp", barang_6)
print("Total harga barang sebelum pajak adalah Rp", total_harga)
print("Total pajak yang harus dibayar adalah Rp", total_pajak)
print("Total harga barang dengan pajak adalah Rp", total_bayar)
print("Rata-rata harga barang dengan pajak adalah Rp", rata_rata)
print("NIM saya adalah", nim)
print("Apakah NIM saya lebih kecil dari rata-rata harga barang?", bolean)
print("Total harga barang dalam Ringgit Malaysia adalah RM", total_ringgit)
print("Total harga barang dalam Swiss Franc adalah CHF", total_franc_swiss)
print("Harga barang ganjil adalah:", barang_ganjil)