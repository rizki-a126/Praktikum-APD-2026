angka = {1, 1, 1, 2, 2, 3,}
print(angka)

nama = ['Andi', 'Andi', 'Citra', 'Siska', 'Citra']
unik = set(nama)

angka = {1, 1, 1, 2, 2, 3,}

for item in angka:
    if item == 1 or item == 2:
        print(item)

angka.add(4)
print(angka)

#gabisa ditambah  diantara data karena set tidak memakai indeks, tidak seperti list

angka.discard(4)
print(angka.discard(4))

#kalau gamau error pake discard, tapi pake remove juga bisa.

angka = {1, 2, 3}

for item in list(angka):
    if item == 3:
        angka.remove(3)
        print(angka) 

angka_genap = {2, 4, 6, 8 ,10}
angkaa = {1, 2, 3, 4, 5}

print(angka_genap.union(angkaa))
print(angka_genap)

print(angkaa.intersection(angkaa))
print(angka_genap & angka)

print(angka_genap.difference(angka))
print(angka.difference(angka_genap))
print(angka_genap - angka)

kendaraan = {
    'Mobil' : 'Innova',
    'Motor' : 'Vario'
}

print(kendaraan)
print(kendaraan['Mobil'])
print(kendaraan.get('Obil'))
for item in kendaraan.values():
    print(item)

for item in kendaraan.items():
    print(item)

for key, value in kendaraan.items():
    print(f"Key {key} : Value {value}")

#kalau pakai tanda kurung siku rawan error, pake get untuk menghindari error

# kendaraann = {
#    'Mobil' : 'Innova'
#    'Motor' : [1, 2, ,3 ,4 ,5 ,6, {
#        'Angka' : [1, 2, 3, 4, 5]
#    }
#}

