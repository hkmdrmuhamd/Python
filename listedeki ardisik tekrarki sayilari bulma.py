liste = []
newlist = []

sayac1 = sayac2 = i = 0
j = 1

boyut = int(input("Kac boyutlu bir liste olusturmak istiyorsunuz:"))

while sayac1 < boyut:
    sayi = int(input("{}. sayiyi giriniz:".format(sayac1+1)))
    liste += [sayi]
    sayac1 += 1

print("Olusturdugunuz {} elemanli liste -> {}".format(boyut,liste))

while sayac2 < len(liste):
    if j < len(liste):
        if liste[i] == liste[j]:
            newlist += [liste[i]]
    i += 1
    j += 1
    sayac2 += 1

print("Listedeki ardisik tekrarli elemanlar -> {}".format(newlist))