makanan = {
    "nasgor" : 15000,
    "bakso" : 20000
}

makanan["sate"] = 25000
#makanan["bakso"] = 25000

makanan.update({
    "rawon" : 25000
    "mie ayam" : 20000})

tambah = makanan.setdefault("naskun", 18000)
#bedanya pake update sm kurung siku, kalau update bisa menambah lebih dari 1 sekaligus
del makanan["bakso"]
#del makanan
hapus = makanan.pop("nasgor")

#makanan.clear()
#clear mirip del makanan cuma ga error aja

makanan2 = makanan.copy()
makanan2["soto"] = 20000

print(makanan)
print(hapus)
print("Jumlah makanan", len(makanan))

menu = "bubur ayam", "papeda", "es teh", "sempol"
harga = 10000

makanan3 = dict.fromkeys(menu, harga)

#kalau pake from keys, keys bisa banyak tapi valuesnya cm bisa 1