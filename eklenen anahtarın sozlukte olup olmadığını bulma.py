sozluk = {"Ad" : "Muhammed","Soyad":"Hukumdar","Yas":20}

ekleme = input("Anahtar olarak eklemek istediginiz degeri giriniz:")

if ekleme in sozluk.keys():
    print("Bu anahtar daha onceden vardır.")

else:
    print(sozluk)