kendaraan = input("Masukkan jenis kendaraan anda: ")

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000
print("Tarif parkir untuk", kendaraan, "adalah Rp", tarif_parkir)