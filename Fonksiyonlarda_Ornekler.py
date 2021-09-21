def frekansBul(liste1,liste2,liste3,liste4):
    kontrolListe = list()
    tekrar = 0
    for i in liste1:
        if i in kontrolListe:
            tekrar += 1
            print("{} sayisi {} kez tekrar etmektedir".format(i, tekrar))
        else:
            kontrolListe += [i]
        tekrar = 0
    for i in liste2:
        if i in kontrolListe:
            tekrar += 1
            print("{} sayisi {} kez tekrar etmektedir".format(i, tekrar))
        else:
            kontrolListe += [i]
        tekrar = 0
    for i in liste3:
        if i in kontrolListe:
            tekrar += 1
            print("{} sayisi {} kez tekrar etmektedir".format(i, tekrar))
        else:
            kontrolListe += [i]
        tekrar = 0
    for i in liste4:
        if i in kontrolListe:
            tekrar += 1
            print("{} sayisi {} kez tekrar etmektedir".format(i,tekrar))
        else:
            kontrolListe += [i]


def ozelSayiBul(set1):
    for i in set1:
        liste = list()
        sayi = str(i)
        for j in sayi:
            liste += [j]
        if liste == liste[::-1]:
            print("{} sayisi palindromik bir sayidir".format(i))

        uzunluk = len(liste)
        if uzunluk == 3:
            basamak1 = int(liste[0])
            basamak2 = int(liste[1])
            basamak3 = int(liste[2])
            carpim = basamak1 ** uzunluk + basamak2 ** uzunluk + basamak3 ** uzunluk
            if carpim == int(i):
                print("{} sayisi armstrong bir sayidir".format(i))
        elif uzunluk == 2:
            basamak1 = int(liste[0])
            basamak2 = int(liste[1])
            carpim = basamak1 ** uzunluk + basamak2 ** uzunluk
            if carpim == int(i):
                print("{} sayisi armstrong bir sayidir".format(i))
        elif uzunluk == 4:
            basamak1 = int(liste[0])
            basamak2 = int(liste[1])
            basamak3 = int(liste[2])
            basamak4 = int(liste[3])
            carpim = basamak1 ** uzunluk + basamak2 ** uzunluk + basamak3 ** uzunluk + basamak4 ** uzunluk
            if carpim == int(i):
                print("{} sayisi armstrong bir sayidir".format(i))
        for k in range(1,i+1):
            toplamPBS = 0
            if i % k == 0:
                toplamPBS += k
                if k == i:
                    print("{} sayisi mukemmel bir sayidir.".format(i))

def EsitDegerBul(dict1):
    kontrol = list()
    for i in dict1.keys():
        if dict1[i] in kontrol:
            print("{} key degerinin karsiligi {} values degeri birden cok kez bulundu".format(i,dict1[i]))
        else:
            kontrol += dict1[i]

"""liste1 = liste2 = liste3 = liste4 = list()
for i in range(0,3):
    sayi = int(input("Bir sayi giriniz"))
    liste1 += [sayi]

for i in range(0,5):
    sayi = int(input("Bir sayi giriniz"))
    liste2 += [sayi]


for i in range(0,4):
    sayi = int(input("Bir sayi giriniz"))
    liste3 += [sayi]

for i in range(0,5):
    sayi = int(input("Bir sayi giriniz"))
    liste4 += [sayi]

frekansBul(liste1,liste2,liste3,liste4)

set1 = {370, 202, 28, 1881, 105, 496, 1251}
ozelSayiBul(set1)"""
dict1 = {1:"P" , 9: "Y", 0:"T" , 5: "H", 7:"Y" , 4: "P"}
EsitDegerBul(dict1)