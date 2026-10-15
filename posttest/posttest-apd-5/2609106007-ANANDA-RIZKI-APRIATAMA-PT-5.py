import os
print('='*22, 'PROGRAM MANAJEMEN DATA HERO MOBILE LEGENDS', '='*22)
print('='*88)
username_admin = "Rawr"
password_admin = "2112"
login = False
username = 'Rizki' #buat test program sebagai user
password = '123'   #buat test program sebagai user
login2 = False
loginuser = False
loginadmin = False
hero_ditemukan = False
data_hero = [
    ["1. Miya", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["2. Balmond", ["Role: Fighter"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["3. Saber", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["4. Alice", ["Role: Mage/Tank"], ["Lane: EXP Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["5. Nana", ["Role: Mage/Support"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["6. Tigreal", ["Role: Tank"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["7. Alucard", ["Role: Fighter/Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["8. Karina", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["9. Akai", ["Role: Tank"], ["Lane: Roam/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["10. Franco", ["Role: Tank/Support"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["11. Bane", ["Role: Fighter/Mage"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical/Magic"], ["Tahun Rilis: 2016"]],
    ["12. Bruno", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["13. Clint", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["14. Rafaela", ["Role: Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["15. Eudora", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["16. Zilong", ["Role: Fighter/Assassin"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["17. Fanny", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["18. Layla", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["19. Minotaur", ["Role: Tank/Support"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["20. Lolita", ["Role: Tank/Support"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["21. Hayabusa", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["22. Freya", ["Role: Fighter"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["23. Gord", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["24. Natalia", ["Role: Assassin"], ["Lane: Jungle/Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["25. Kagura", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["26. Chou", ["Role: Fighter"], ["Lane: EXP Lane/Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2016"]],
    ["27. Johnson", ["Role: Tank"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["28. Yi Sun-shin", ["Role: Assassin/Marksman"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["29. Cyclops", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2016"]],
    ["30. Estes", ["Role: Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["31. Hilda", ["Role: Fighter/Tank"], ["Lane: EXP Lane/Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["32. Aurora", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["33. Lapu-Lapu", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["34. Vexana", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["35. Roger", ["Role: Fighter/Marksman"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["36. Karrie", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical/True"], ["Tahun Rilis: 2017"]],
    ["37. Gatotkaca", ["Role: Tank/Fighter"], ["Lane: EXP Lane/Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["38. Harley", ["Role: Assassin/Mage"], ["Lane: Jungle"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["39. Irithel", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["40. Grock", ["Role: Tank"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["41. Argus", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["42. Odette", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["43. Lancelot", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["44. Diggie", ["Role: Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["45. Hylos", ["Role: Tank"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["46. Zhask", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2017"]],
    ["47. Helcurt", ["Role: Assassin"], ["Lane: Jungle/Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2017"]],
    ["48. Pharsa", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["49. Lesley", ["Role: Marksman/Assassin"], ["Lane: Gold Lane"], ["Tipe Damage: Physical/True"], ["Tahun Rilis: 2018"]],
    ["50. Jawhead", ["Role: Fighter"], ["Lane: EXP Lane/Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["51. Angela", ["Role: Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["52. Gusion", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["53. Valir", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["54. Martis", ["Role: Fighter"], ["Lane: Jungle/EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["55. Uranus", ["Role: Tank"], ["Lane: EXP Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["56. Hanabi", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["57. Chang'e", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["58. Kaja", ["Role: Fighter/Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["59. Selena", ["Role: Assassin/Mage"], ["Lane: Jungle/Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["60. Aldous", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["61. Claude", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["62. Vale", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["63. Leomord", ["Role: Fighter"], ["Lane: Jungle/EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["64. Lunox", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["65. Hanzo", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["66. Belerick", ["Role: Tank"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["67. Kimmy", ["Role: Marksman/Mage"], ["Lane: Gold Lane"], ["Tipe Damage: Physical/Magic"], ["Tahun Rilis: 2018"]],
    ["68. Thamuz", ["Role: Fighter"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["69. Harith", ["Role: Mage"], ["Lane: Gold Lane/Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["70. Minsitthar", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2018"]],
    ["71. Kadita", ["Role: Mage/Assassin"], ["Lane: Mid Lane/Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["72. Faramis", ["Role: Support/Mage"], ["Lane: Roam/Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2018"]],
    ["73. Badang", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["74. Khufra", ["Role: Tank"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["75. Granger", ["Role: Marksman"], ["Lane: Gold Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["76. Guinevere", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2019"]],
    ["77. Esmeralda", ["Role: Tank/Mage"], ["Lane: EXP Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2019"]],
    ["78. Terizla", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["79. X.Borg", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: True/Physical"], ["Tahun Rilis: 2019"]],
    ["80. Ling", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["81. Dyrroth", ["Role: Fighter"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["82. Lylia", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2019"]],
    ["83. Baxia", ["Role: Tank"], ["Lane: Jungle/Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2019"]],
    ["84. Masha", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["85. Wanwan", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2019"]],
    ["86. Silvanna", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2019"]],
    ["87. Cecilion", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2020"]],
    ["88. Carmilla", ["Role: Support/Tank"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2020"]],
    ["89. Atlas", ["Role: Tank"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2020"]],
    ["90. Popol and Kupa", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2020"]],
    ["91. Yu Zhong", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2020"]],
    ["92. Luo Yi", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2020"]],
    ["93. Benedetta", ["Role: Assassin"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2020"]],
    ["94. Khaleed", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2020"]],
    ["95. Barats", ["Role: Tank/Fighter"], ["Lane: Jungle/EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2020"]],
    ["96. Brody", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2020"]],
    ["97. Yve", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2021"]],
    ["98. Mathilda", ["Role: Support/Assassin"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2020"]],
    ["99. Paquito", ["Role: Fighter"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2021"]],
    ["100. Gloo", ["Role: Tank"], ["Lane: EXP Lane/Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2021"]],
    ["101. Beatrix", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2021"]],
    ["102. Phoveus", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2021"]],
    ["103. Natan", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2021"]],
    ["104. Aulus", ["Role: Fighter"], ["Lane: Jungle/EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2021"]],
    ["105. Aamon", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2021"]],
    ["106. Floryn", ["Role: Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2021"]],
    ["107. Yin", ["Role: Fighter"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2022"]],
    ["108. Melissa", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2022"]],
    ["109. Xavier", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2022"]],
    ["110. Julian", ["Role: Fighter/Assassin"], ["Lane: Jungle/EXP Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2022"]],
    ["111. Fredrinn", ["Role: Fighter/Tank"], ["Lane: Jungle/EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2022"]],
    ["112. Joy", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2022"]],
    ["113. Novaria", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2023"]],
    ["114. Arlott", ["Role: Fighter/Assassin"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2023"]],
    ["115. Ixia", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2023"]],
    ["116. Nolan", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2023"]],
    ["117. Cici", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2023"]],
    ["118. Chip", ["Role: Tank/Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2024"]],
    ["119. Zhuxin", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2024"]],
    ["120. Suyou", ["Role: Fighter/Assassin"], ["Lane: Jungle/EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2024"]],
    ["121. Lukas", ["Role: Fighter"], ["Lane: EXP Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2024"]],
    ["122. Kalea", ["Role: Support/Fighter"], ["Lane: Roam"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2025"]],
    ["123. Zetian", ["Role: Mage"], ["Lane: Mid Lane"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2025"]],
    ["124. Obsidia", ["Role: Marksman"], ["Lane: Gold Lane"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2025"]],
    ["125. Sora", ["Role: Fighter/Assassin"], ["Lane: EXP Lane/Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2025"]],
    ["126. Marcel", ["Role: Support"], ["Lane: Roam"], ["Tipe Damage: Magic"], ["Tahun Rilis: 2025"]],
    ["127. Hirara", ["Role: Assassin"], ["Lane: Jungle"], ["Tipe Damage: Physical"], ["Tahun Rilis: 2026"]]
]

# for i in data_hero:
    # print(i[0], "[", i [1][0],"]", "[", i[2][0], "]", "[", i[3][0], "]", "[", i[4][0], "]")
os.system('cls' if os.name == 'nt' else 'clear')
while login != True:
    print('='*22, "Selamat datang!", "="*22)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Masukkan Pilihan (1/2/3): ")
    if pilihan == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('='*22, 'LAMAN REGISTER', '='*22)
        username = input('Buat Username: ')
        password = input('Buat Password: ')
        print("Silahkan login kembali.")
    elif pilihan == "1":
        while login2 != True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('='*22, 'LOGIN', '='*22)
            usn_login = input('Masukkan Username: ')
            pw_login = input('Masukkan Password: ')
            if usn_login == username and pw_login == password:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('='*22, 'Login berhasil.', '='*22)
                loginuser = True
                login2 = True
                login = True
                break
            elif usn_login == username_admin and pw_login == password_admin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('='*22, 'Selamat Datang Admin.', '='*22)
                login = True
                login2 = True
                loginadmin = True
                break
            elif usn_login != username or pw_login != password:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Username atau Password salah atau tidak terdaftar! Silahkan coba lagi.')
                break
    else: 
        break

while loginadmin == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('='*44)
    print('='*19, 'MENU', '='*19)
    print('='*44)
    print('1. Menambah Data Hero')
    print('2. Melihat Daftar Data Hero')
    print('3. Menghapus Data Hero')
    print('4. Keluar')
    menu = input('Masukkan Pilihan (1/2/3/4): ')
    if menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in data_hero:
            print(f'{i[0]} = [{i[1][0]}], [{i[2][0]}], [{i[3][0]}], [{i[4][0]}]')
        print('='*44)
        hasil = input("Kembali ke menu? (y/n)")
        if hasil == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            login = False
            break
    elif menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('='*22, 'TAMBAH DATA HERO', '='*22)
        nomor_baru = len(data_hero) + 1
        nama_input = input("Masukkan Nama Hero: ")
        nama_hero_baru = str(nomor_baru) + ". " + nama_input
        role_input = input("Masukkan Role Hero: ")
        lane_input = input("Masukkan Lane Hero: ")
        damage_input = input("Masukkan Tipe Damage: ")
        tahun_input = input("Masukkan Tahun Rilis: ")
        hero_baru = [
            nama_hero_baru, 
            ["Role: " + role_input], 
            ["Lane: " + lane_input], 
            ["Tipe Damage: " + damage_input], 
            ["Tahun Rilis: " + tahun_input]
        ]
        data_hero.append(hero_baru)
        print('='*44)
        print("Data hero berhasil ditambahkan.")
        hasil = input("Kembali ke menu? (y/n): ")
        if hasil == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            login = False
            break
    elif menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        nama_hapus = input("Masukkan Nama Hero yang ingin dihapus (Contoh: Miya): ")
        for i in data_hero:
            if nama_hapus in i[0]:
                nama_target = i[0]
                data_hero.remove(i)
                print('='*44)
                print("Sukses menghapus data:", nama_target)
                hero_ditemukan = True
                break 
        if hero_ditemukan == False:
            print('='*44)
            print("Gagal! Nama hero tidak ditemukan.")
        nomor_sekarang = 1
        for i in data_hero:
            nama_lengkap = i[0]
            index_titik = 0
            for karakter in nama_lengkap:
                if karakter == ".":
                    break
                index_titik += 1
            nama_murni = nama_lengkap[index_titik + 2:]
            i[0] = str(nomor_sekarang) + ". " + nama_murni
            nomor_sekarang += 1
        hasil = input("Kembali ke menu? (y/n): ")
        if hasil == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            login = False
            break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        login = False
        break

while loginuser == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('='*44)
    print('='*19, 'MENU', '='*19)
    print('='*44)
    print('1. Melihat Daftar Data Hero')
    print('2. Keluar')
    menu = input('Masukkan Pilihan (1/2): ')
    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in data_hero:
            print(f'{i[0]} = [{i[1][0]}], [{i[2][0]}], [{i[3][0]}], [{i[4][0]}]')
        print('='*44)
        hasil = input("Kembali ke menu? (y/n)")
        if hasil == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            login = False
            break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        loginuser = False
        break