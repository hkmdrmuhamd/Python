def kullanici(kullanici_sayisi):

    for j in range(1, kullanici_sayisi + 1):
        keySayisi = int(input("Kac adet key degeri eklemek istersiniz:"))
        for i in range(1, keySayisi + 1):
            key = input("{}.Key degeri giriniz:".format(i))
            values = input("{}. Kullanici ile ilgili values degerini giriniz:".format(i))
            bilgiler.update({key: values})
    return bilgiler

bilgiler = dict()

Sayi = int(input("Kac adet kullanici eklemek istersiniz:"))
print(kullanici(Sayi))