import os

print('='*22, 'PROGRAM MANAJEMEN DATA HERO MOBILE LEGENDS', '='*22)
print('='*88)

username_admin = "Rawr"
password_admin = "2112"
login = False
username = 'Rizki' # buat test program sebagai user
password = '123'   # buat test program sebagai user
login2 = False
loginuser = False
loginadmin = False
hero_ditemukan = False
data_hero = {
    1: {"nama": "Miya", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2016"},
    2: {"nama": "Balmond", "role": "Fighter", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2016"},
    3: {"nama": "Saber", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2016"},
    4: {"nama": "Alice", "role": "Mage/Tank", "lane": "EXP Lane", "damage": "Magic", "tahun": "2016"},
    5: {"nama": "Nana", "role": "Mage/Support", "lane": "Mid Lane", "damage": "Magic", "tahun": "2016"},
    6: {"nama": "Tigreal", "role": "Tank", "lane": "Roam", "damage": "Physical", "tahun": "2016"},
    7: {"nama": "Alucard", "role": "Fighter/Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2016"},
    8: {"nama": "Karina", "role": "Assassin", "lane": "Jungle", "damage": "Magic", "tahun": "2016"},
    9: {"nama": "Akai", "role": "Tank", "lane": "Roam/Jungle", "damage": "Physical", "tahun": "2016"},
    10: {"nama": "Franco", "role": "Tank/Support", "lane": "Roam", "damage": "Physical", "tahun": "2016"},
    11: {"nama": "Bane", "role": "Fighter/Mage", "lane": "EXP Lane/Jungle", "damage": "Physical/Magic", "tahun": "2016"},
    12: {"nama": "Bruno", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2016"},
    13: {"nama": "Clint", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2016"},
    14: {"nama": "Rafaela", "role": "Support", "lane": "Roam", "damage": "Magic", "tahun": "2016"},
    15: {"nama": "Eudora", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2016"},
    16: {"nama": "Zilong", "role": "Fighter/Assassin", "lane": "EXP Lane", "damage": "Physical", "tahun": "2016"},
    17: {"nama": "Fanny", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2016"},
    18: {"nama": "Layla", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2016"},
    19: {"nama": "Minotaur", "role": "Tank/Support", "lane": "Roam", "damage": "Physical", "tahun": "2016"},
    20: {"nama": "Lolita", "role": "Tank/Support", "lane": "Roam", "damage": "Physical", "tahun": "2016"},
    21: {"nama": "Hayabusa", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2016"},
    22: {"nama": "Freya", "role": "Fighter", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2016"},
    23: {"nama": "Gord", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2016"},
    24: {"nama": "Natalia", "role": "Assassin", "lane": "Jungle/Roam", "damage": "Physical", "tahun": "2016"},
    25: {"nama": "Kagura", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2016"},
    26: {"nama": "Chou", "role": "Fighter", "lane": "EXP Lane/Roam", "damage": "Physical", "tahun": "2016"},
    27: {"nama": "Johnson", "role": "Tank", "lane": "Roam", "damage": "Physical", "tahun": "2017"},
    28: {"nama": "Yi Sun-shin", "role": "Assassin/Marksman", "lane": "Jungle", "damage": "Physical", "tahun": "2017"},
    29: {"nama": "Cyclops", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2016"},
    30: {"nama": "Estes", "role": "Support", "lane": "Roam", "damage": "Magic", "tahun": "2017"},
    31: {"nama": "Hilda", "role": "Fighter/Tank", "lane": "EXP Lane/Roam", "damage": "Physical", "tahun": "2017"},
    32: {"nama": "Aurora", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2017"},
    33: {"nama": "Lapu-Lapu", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2017"},
    34: {"nama": "Vexana", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2017"},
    35: {"nama": "Roger", "role": "Fighter/Marksman", "lane": "Jungle", "damage": "Physical", "tahun": "2017"},
    36: {"nama": "Karrie", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical/True", "tahun": "2017"},
    37: {"nama": "Gatotkaca", "role": "Tank/Fighter", "lane": "EXP Lane/Roam", "damage": "Magic", "tahun": "2017"},
    38: {"nama": "Harley", "role": "Assassin/Mage", "lane": "Jungle", "damage": "Magic", "tahun": "2017"},
    39: {"nama": "Irithel", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2017"},
    40: {"nama": "Grock", "role": "Tank", "lane": "Roam", "damage": "Physical", "tahun": "2017"},
    41: {"nama": "Argus", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2017"},
    42: {"nama": "Odette", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2017"},
    43: {"nama": "Lancelot", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2017"},
    44: {"nama": "Diggie", "role": "Support", "lane": "Roam", "damage": "Magic", "tahun": "2017"},
    45: {"nama": "Hylos", "role": "Tank", "lane": "Roam", "damage": "Magic", "tahun": "2017"},
    46: {"nama": "Zhask", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2017"},
    47: {"nama": "Helcurt", "role": "Assassin", "lane": "Jungle/Roam", "damage": "Physical", "tahun": "2017"},
    48: {"nama": "Pharsa", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2018"},
    49: {"nama": "Lesley", "role": "Marksman/Assassin", "lane": "Gold Lane", "damage": "Physical/True", "tahun": "2018"},
    50: {"nama": "Jawhead", "role": "Fighter", "lane": "EXP Lane/Roam", "damage": "Physical", "tahun": "2018"},
    51: {"nama": "Angela", "role": "Support", "lane": "Roam", "damage": "Magic", "tahun": "2018"},
    52: {"nama": "Gusion", "role": "Assassin", "lane": "Jungle", "damage": "Magic", "tahun": "2018"},
    53: {"nama": "Valir", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2018"},
    54: {"nama": "Martis", "role": "Fighter", "lane": "Jungle/EXP Lane", "damage": "Physical", "tahun": "2018"},
    55: {"nama": "Uranus", "role": "Tank", "lane": "EXP Lane", "damage": "Magic", "tahun": "2018"},
    56: {"nama": "Hanabi", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2018"},
    57: {"nama": "Chang'e", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2018"},
    58: {"nama": "Kaja", "role": "Fighter/Support", "lane": "Roam", "damage": "Magic", "tahun": "2018"},
    59: {"nama": "Selena", "role": "Assassin/Mage", "lane": "Jungle/Roam", "damage": "Magic", "tahun": "2018"},
    60: {"nama": "Aldous", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2018"},
    61: {"nama": "Claude", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2018"},
    62: {"nama": "Vale", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2018"},
    63: {"nama": "Leomord", "role": "Fighter", "lane": "Jungle/EXP Lane", "damage": "Physical", "tahun": "2018"},
    64: {"nama": "Lunox", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2018"},
    65: {"nama": "Hanzo", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2018"},
    66: {"nama": "Belerick", "role": "Tank", "lane": "Roam", "damage": "Magic", "tahun": "2018"},
    67: {"nama": "Kimmy", "role": "Marksman/Mage", "lane": "Gold Lane", "damage": "Physical/Magic", "tahun": "2018"},
    68: {"nama": "Thamuz", "role": "Fighter", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2018"},
    69: {"nama": "Harith", "role": "Mage", "lane": "Gold Lane/Mid Lane", "damage": "Magic", "tahun": "2018"},
    70: {"nama": "Minsitthar", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2018"},
    71: {"nama": "Kadita", "role": "Mage/Assassin", "lane": "Mid Lane/Roam", "damage": "Magic", "tahun": "2018"},
    72: {"nama": "Faramis", "role": "Support/Mage", "lane": "Roam/Mid Lane", "damage": "Magic", "tahun": "2018"},
    73: {"nama": "Badang", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2019"},
    74: {"nama": "Khufra", "role": "Tank", "lane": "Roam", "damage": "Physical", "tahun": "2019"},
    75: {"nama": "Granger", "role": "Marksman", "lane": "Gold Lane/Jungle", "damage": "Physical", "tahun": "2019"},
    76: {"nama": "Guinevere", "role": "Fighter", "lane": "EXP Lane", "damage": "Magic", "tahun": "2019"},
    77: {"nama": "Esmeralda", "role": "Tank/Mage", "lane": "EXP Lane", "damage": "Magic", "tahun": "2019"},
    78: {"nama": "Terizla", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2019"},
    79: {"nama": "X.Borg", "role": "Fighter", "lane": "EXP Lane", "damage": "True/Physical", "tahun": "2019"},
    80: {"nama": "Ling", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2019"},
    81: {"nama": "Dyrroth", "role": "Fighter", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2019"},
    82: {"nama": "Lylia", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2019"},
    83: {"nama": "Baxia", "role": "Tank", "lane": "Jungle/Roam", "damage": "Magic", "tahun": "2019"},
    84: {"nama": "Masha", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2019"},
    85: {"nama": "Wanwan", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2019"},
    86: {"nama": "Silvanna", "role": "Fighter", "lane": "EXP Lane", "damage": "Magic", "tahun": "2019"},
    87: {"nama": "Cecilion", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2020"},
    88: {"nama": "Carmilla", "role": "Support/Tank", "lane": "Roam", "damage": "Magic", "tahun": "2020"},
    89: {"nama": "Atlas", "role": "Tank", "lane": "Roam", "damage": "Magic", "tahun": "2020"},
    90: {"nama": "Popol and Kupa", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2020"},
    91: {"nama": "Yu Zhong", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2020"},
    92: {"nama": "Luo Yi", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2020"},
    93: {"nama": "Benedetta", "role": "Assassin", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2020"},
    94: {"nama": "Khaleed", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2020"},
    95: {"nama": "Barats", "role": "Tank/Fighter", "lane": "Jungle/EXP Lane", "damage": "Physical", "tahun": "2020"},
    96: {"nama": "Brody", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2020"},
    97: {"nama": "Yve", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2021"},
    98: {"nama": "Mathilda", "role": "Support/Assassin", "lane": "Roam", "damage": "Magic", "tahun": "2020"},
    99: {"nama": "Paquito", "role": "Fighter", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2021"},
    100: {"nama": "Gloo", "role": "Tank", "lane": "EXP Lane/Roam", "damage": "Magic", "tahun": "2021"},
    101: {"nama": "Beatrix", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2021"},
    102: {"nama": "Phoveus", "role": "Fighter", "lane": "EXP Lane", "damage": "Magic", "tahun": "2021"},
    103: {"nama": "Natan", "role": "Marksman", "lane": "Gold Lane", "damage": "Magic", "tahun": "2021"},
    104: {"nama": "Aulus", "role": "Fighter", "lane": "Jungle/EXP Lane", "damage": "Physical", "tahun": "2021"},
    105: {"nama": "Aamon", "role": "Assassin", "lane": "Jungle", "damage": "Magic", "tahun": "2021"},
    106: {"nama": "Floryn", "role": "Support", "lane": "Roam", "damage": "Magic", "tahun": "2021"},
    107: {"nama": "Yin", "role": "Fighter", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2022"},
    108: {"nama": "Melissa", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2022"},
    109: {"nama": "Xavier", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2022"},
    110: {"nama": "Julian", "role": "Fighter/Assassin", "lane": "Jungle/EXP Lane", "damage": "Magic", "tahun": "2022"},
    111: {"nama": "Fredrinn", "role": "Fighter/Tank", "lane": "Jungle/EXP Lane", "damage": "Physical", "tahun": "2022"},
    112: {"nama": "Joy", "role": "Assassin", "lane": "Jungle", "damage": "Magic", "tahun": "2022"},
    113: {"nama": "Novaria", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2023"},
    114: {"nama": "Arlott", "role": "Fighter/Assassin", "lane": "EXP Lane", "damage": "Physical", "tahun": "2023"},
    115: {"nama": "Ixia", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2023"},
    116: {"nama": "Nolan", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2023"},
    117: {"nama": "Cici", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2023"},
    118: {"nama": "Chip", "role": "Tank/Support", "lane": "Roam", "damage": "Magic", "tahun": "2024"},
    119: {"nama": "Zhuxin", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2024"},
    120: {"nama": "Suyou", "role": "Fighter/Assassin", "lane": "Jungle/EXP Lane", "damage": "Physical", "tahun": "2024"},
    121: {"nama": "Lukas", "role": "Fighter", "lane": "EXP Lane", "damage": "Physical", "tahun": "2024"},
    122: {"nama": "Kalea", "role": "Support/Fighter", "lane": "Roam", "damage": "Physical", "tahun": "2025"},
    123: {"nama": "Zetian", "role": "Mage", "lane": "Mid Lane", "damage": "Magic", "tahun": "2025"},
    124: {"nama": "Obsidia", "role": "Marksman", "lane": "Gold Lane", "damage": "Physical", "tahun": "2025"},
    125: {"nama": "Sora", "role": "Fighter/Assassin", "lane": "EXP Lane/Jungle", "damage": "Physical", "tahun": "2025"},
    126: {"nama": "Marcel", "role": "Support", "lane": "Roam", "damage": "Magic", "tahun": "2025"},
    127: {"nama": "Hirara", "role": "Assassin", "lane": "Jungle", "damage": "Physical", "tahun": "2026"}
}

# # os.system('cls' if os.name == 'nt' else 'clear')
# # while login != True:
# #     print('='*22, "Selamat datang!", "="*22)
# #     print("1. Login")
# #     print("2. Register")
# #     print("3. Keluar")
# #     pilihan = input("Masukkan Pilihan (1/2/3): ")
# #     if pilihan == "2":
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         print('='*22, 'LAMAN REGISTER', '='*22)
# #         username = input('Buat Username: ')
# #         password = input('Buat Password: ')
# #         print("Silahkan login kembali.")
# #     elif pilihan == "1":
# #         while login2 != True:
# #             os.system('cls' if os.name == 'nt' else 'clear')
# #             print('='*22, 'LOGIN', '='*22)
# #             usn_login = input('Masukkan Username: ')
# #             pw_login = input('Masukkan Password: ')
# #             if usn_login == username and pw_login == password:
# #                 os.system('cls' if os.name == 'nt' else 'clear')
# #                 print('='*22, 'Login berhasil.', '='*22)
# #                 loginuser = True
# #                 login2 = True
# #                 login = True
# #                 break
# #             elif usn_login == username_admin and pw_login == password_admin:
# #                 os.system('cls' if os.name == 'nt' else 'clear')
# #                 print('='*22, 'Selamat Datang Admin.', '='*22)
# #                 login = True
# #                 login2 = True
# #                 loginadmin = True
# #                 break
# #             elif usn_login != username or pw_login != password:
# #                 os.system('cls' if os.name == 'nt' else 'clear')
# #                 print('Username atau Password salah atau tidak terdaftar! Silahkan coba lagi.')
# #                 break
# #     else: 
# #         break

# # while loginadmin == True:
# #     os.system('cls' if os.name == 'nt' else 'clear')
# #     print('='*44)
# #     print('='*19, 'MENU', '='*19)
# #     print('='*44)
# #     print('1. Menambah Data Hero')
# #     print('2. Melihat Daftar Data Hero')
# #     print('3. Menghapus Data Hero')
# #     print('4. Keluar')
# #     menu = input('Masukkan Pilihan (1/2/3/4): ')
# #     if menu == "2":
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         for key, value in data_hero.items():
# #             print(f"{key}. {value['nama']} = [Role: {value['role']}], [Lane: {value['lane']}], [Tipe Damage: {value['damage']}], [Tahun Rilis: {value['tahun']}]")
# #         print('='*44)
# #         hasil = input("Kembali ke menu? (y/n): ")
# #         if hasil == "n":
# #             os.system('cls' if os.name == 'nt' else 'clear')
# #             login = False
# #             break
# #     elif menu == "1":
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         print('='*22, 'TAMBAH DATA HERO', '='*22)
# #         nomor_baru = len(data_hero) + 1
# #         nama_input = input("Masukkan Nama Hero: ")
# #         role_input = input("Masukkan Role Hero: ")
# #         lane_input = input("Masukkan Lane Hero: ")
# #         damage_input = input("Masukkan Tipe Damage: ")
# #         tahun_input = input("Masukkan Tahun Rilis: ")
# #         data_hero[nomor_baru] = {
# #             "nama": nama_input,
# #             "role": role_input,
# #             "lane": lane_input,
# #             "damage": damage_input,
# #             "tahun": tahun_input
# #         }
# #         print('='*44)
# #         print("Data hero berhasil ditambahkan.")
# #         hasil = input("Kembali ke menu? (y/n): ")
# #         if hasil == "n":
# #             os.system('cls' if os.name == 'nt' else 'clear')
# #             login = False
# #             break
# #     elif menu == "3":
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         nama_hapus = input("Masukkan Nama Hero yang ingin dihapus (Contoh: Miya): ")
# #         for key, value in data_hero.items():
# #             if nama_hapus == value['nama']:
# #                 key_hapus = key
# #                 nama_target = value['nama']
# #                 hero_ditemukan = True
# #                 break
# #         if hero_ditemukan == True:
# #             del data_hero[key_hapus]
# #             print('='*44)
# #             print("Sukses menghapus data:", nama_target)
#             urut_data = {}
#             key_ulang = 1
#             for key in data_hero.keys():
#                 urut_data[key_ulang]
#                 key_ulang += 1
#                 for key in data_hero.keys():
#                 print(urut_data[key_ulang])
# #             data_hero = urut_data
# #         else:
# #             print('='*44)
# #             print("Gagal! Nama hero tidak ditemukan.")
# #         hasil = input("Kembali ke menu? (y/n): ")
# #         if hasil == "n":
# #             os.system('cls' if os.name == 'nt' else 'clear')
# #             login = False
# #             break
# #     else:
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         login = False
# #         break

# # while loginuser == True:
# #     os.system('cls' if os.name == 'nt' else 'clear')
# #     print('='*44)
# #     print('='*19, 'MENU', '='*19)
# #     print('='*44)
# #     print('1. Melihat Daftar Data Hero')
# #     print('2. Keluar')
# #     menu = input('Masukkan Pilihan (1/2): ')
# #     if menu == "1":
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         for key, value in data_hero.items():
# #             print(f"{key}. {value['nama']} = [Role: {value['role']}], [Lane: {value['lane']}], [Tipe Damage: {value['damage']}], [Tahun Rilis: {value['tahun']}]")
# #         print('='*44)
# #         hasil = input("Kembali ke menu? (y/n): ")
# #         if hasil == "n":
# #             os.system('cls' if os.name == 'nt' else 'clear')
# #             login = False
# #             break
# #     else:
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         loginuser = False
# #         break
urut_data = {}
key_ulang = 1
for key in data_hero.keys():
    urut_data[key_ulang]
    key_ulang += 1
    for key in data_hero.keys():
        print(urut_data[key_ulang])