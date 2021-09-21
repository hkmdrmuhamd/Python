#OB sayisi bir sayinin karesi ya da 11 in katlari olan sayilara verilen isimdir.
liste  = []
sayi1 = int(input("Baslangic degerini giriniz:"))
sayi2 = int(input("Bitis degerini giriniz:"))

sayac = sayi1 + 1
sayac2 = sayi1 + 1
i = 2

while sayi1 < sayac < sayi2:
    if sayac % 11 == 0:
        liste += [sayac]
    sayac += 1
while sayi1 < sayac2 < sayi2:
    while i < sayac2:
        if i * i  == sayac2:
            liste += [sayac2]
        i += 1
        sayac2 += 1
    sayac2 += 1


print("Girdiginiz araliktaki OB sayilari -> {}".format(liste))