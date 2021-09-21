liste = []
newliste = []
sayac = i = sayac2 = 0
j = 1
boyut = int(input("Kac sayi girmek istersiniz ->"))

while sayac < boyut:
    sayi = int(input("{}. sayiyi giriniz:".format(sayac+1)))
    liste += [sayi]
    sayac += 1
print("Girdiginiz sayilarda olusan liste -> {}".format(liste))

while sayac2 < boyut:
    if j <= len(liste):
        sayi1 = liste[i]
        sayi2 = liste[j]
    if sayi1 < sayi2:
        if sayi2 not in newliste:
            newliste += [sayi2]
            i += 1
            j += 1
    else:
        if sayi1 not in newliste:
            newliste += [sayi1]
            i += 1
            j += 1
    sayac2 += 1

print("Yukselen sayilardan olusan yeni liste -> {}".format(newliste))