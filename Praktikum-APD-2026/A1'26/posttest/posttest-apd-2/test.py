kendaraan = input("Masukkan jenis kendaraan anda: ")

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000
print("Tarif parkir untuk", kendaraan, "adalah Rp", tarif_parkir)


usia = int(input("Masukkan usia pengunjung: "))
if usia >= 16:
    print("Silahkan masuk")
else:
    print("Dilarang masuk") 

usia = print("Silahkan masuk") if int(input("Masukkan usia anda: ")) >= 16 else print("Dilarang masuk")