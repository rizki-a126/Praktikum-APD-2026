username = "Rizki"
password = "007"
batas = 3
saldo = 5000000
pin = "007007"
batas_pin = 3

while batas > 0:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username != "Rizki" and password != "007":
        print("Username dan password salah!")
        print("3 kali salah, maka akun Anda akan diblokir.")
    elif username != "Rizki":
        print("Username salah!")
        print("3 kali salah, maka akun Anda akan diblokir.")
    elif password != "007":
        print("Password salah!")
        print("3 kali salah, maka akun Anda akan diblokir.")
    batas -= 1
    if batas == 0:
        print("Kesempatan habis, akun Anda diblokir.")
        break
    if username == "Rizki" and password == "007":
        print("Login berhasil!")
        print("="*44)
        print("Pilih menu:")
        print("1. Transfer uang")
        print("2. Logout")
        menu = input("Masukkan pilihan: ")
        while menu != "1" and menu != "2":
            print("Pilihan tidak valid. Silakan coba lagi.")
            menu = input("Masukkan pilihan: ")
        while menu == "1" or menu == "2":
            if menu == "1":
                print("="*44)
                print("Saldo Anda saat ini: Rp", saldo)
                penerima = input("Masukkan username penerima: ")
                nominal = int(input("Masukkan nominal transfer: Rp "))
                if nominal < 50000:
                    print("Minimal transfer Rp50.000,00. Silakan coba lagi.")
                elif nominal > 1000000 and nominal <= saldo:
                    print("Maksimal transfer Rp1.000.000,00. Silakan coba lagi.")
                elif nominal > saldo:
                    print("Saldo tidak mencukupi. Silakan coba lagi.")
                else:
                    while batas_pin > 0:
                        pin = input("Masukkan PIN anda: ")
                        if pin != "007007":
                            print("PIN salah! Silahkan coba lagi.")
                            batas_pin -= 1
                            if batas_pin == 0:
                                print("Kesempatan habis, akun Anda diblokir.")
                                menu = 0
                                batas = 0
                                username = " "
                                break
                        else:
                            saldo -= nominal
                            print("="*22, "STRUK TRANSFER", "="*22)
                            print("Username:", username)
                            print("Penerima:", penerima)
                            print("Nominal transfer: Rp", nominal)
                            print("="*44)
                            transaksi = input("Apakah Anda ingin melakukan transaksi lagi? (y/n): ")
                            if transaksi == "y":
                                menu = "1"
                                break
                            elif transaksi == "n":
                                print("Terima kasih!")
                                batas = 0
                                menu = 0
                                username = " "
                                break
            elif menu == "2":
                menu = 0
                batas = 0
                username = " "
                break
