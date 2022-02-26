import random
kelimeler = ["mersin","mugla","malatya","yozgat","hain","reiner","mikasa","levi"]
rastgele = random.randint(0,7)
kelime = kelimeler[rastgele]
print("Kelimeniz belirlendi..")
tmp = list()
dizi = list()

for i in kelime:
    dizi += [i]

for i in range(0,len(dizi)):
    tmp += ["_"]

print(tmp)
can = len(dizi)
sayici = 0

for i in dizi:
    tahmin = str(input("Lutfen tahmininzi giriniz:"))
    if(tahmin in dizi):
        for i in range(len(dizi)):
            if tahmin == dizi[i]:
                tmp[i] = tahmin
                sayici += 1
    else:
        can -= 1
        print("Can:",can)

    if sayici == len(kelime):
        print("Kazandiniz\n",kelime)

    if (can == 0):
        print("Kaybettiniz\n",kelime)
    print(tmp)