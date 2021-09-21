liste = []
newliste = []
sayac = 0

boyut = int(input("Kac sayi girmek istersiniz ->"))

while sayac < boyut:
    sayi = int(input("{}. sayiyi giriniz:".format(sayac+1)))
    liste += [sayi]
    sayac += 1

for i in liste:
    if i % 2 != 0:
        newliste += [i]

print("Girdiginz sayilardaki tek sayilar -> {}".format(newliste))