nama = input("Masukkan nama Anda: ")

umur = int(input("Masukkan umur Anda: "))
if umur < 13:
    print("Mohon maaf, Anda belum cukup umur untuk menonton")
else:
    jenis_tiket = input("Masukkan jenis tiket (Reguler/Premium/VIP): ")
    if jenis_tiket != "Reguler" and jenis_tiket != "Premium" and jenis_tiket != "VIP" :
        print("Jenis tiket tidak dikenali, silahkan periksa kembali")
    else: 
        if jenis_tiket == "Reguler":
            harga = 50000
        elif jenis_tiket == "Premium":
            harga = 75000
        else:
            harga = 100000

        status_member = input("Status member (Ya/Tidak): ")
        diskon = harga * 0.2 if status_member == "Ya" else 0
        biaya_admin = 0 if status_member == "Ya" else 2000
        status_member = "Aktif" if status_member == "Ya" else "Tidak Tersedia"

        total_bayar = int(harga - diskon + biaya_admin)
        print("Total bayar: ", total_bayar)

        nominal_uang_bayar = int(input("Masukkan nominal uang bayar: "))
        if nominal_uang_bayar < total_bayar:
            print("Nominal pembayaran Anda tidak cukup!")
        else:
            if nominal_uang_bayar == total_bayar:
                kembalian = 0
            else:
                kembalian = nominal_uang_bayar - total_bayar

            print("=======================STRUK PEMBAYARAN========================")
            print("Nama:", nama)
            print("Umur:", umur)
            print("Jenis tiket:", jenis_tiket)
            print("Status member:", status_member)
            print("Nominal pembayaran Anda:", total_bayar)
            print("Kembalian:", kembalian)
            print("===============================================================")