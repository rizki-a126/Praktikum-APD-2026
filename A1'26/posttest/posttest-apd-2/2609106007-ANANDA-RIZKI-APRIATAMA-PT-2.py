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
print("Total harga yang harus dibayar adalah Rp", total_bayar)

rata_rata = total_bayar / len(total_barang)
print("Rata-rata harga barang dengan pajak adalah Rp", rata_rata)

nim = 7
boolean = nim < rata_rata
print("Apakah NIM lebih kecil dari rata-rata harga barang?", boolean)

total_ringgit = total_bayar / 4360
print("Total harga dalam Ringgit Malaysia adalah RM", total_ringgit)

total_franc_swiss = total_bayar / 21665.05
print("Total harga dalam Swiss Franc adalah CHF", total_franc_swiss)

barang_ganjil = total_barang[0:5:2]
print("Harga barang ganjil adalah:", barang_ganjil)