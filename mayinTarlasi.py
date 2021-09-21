                                         #Muhammed Hukumdar - 20010011067

import random
while True:
    oyun_alani = list()
    mayin = list()

    while True:
        boyut = int(input("Oyun Alani:"))
        if boyut < 10:
            print("Oyun alanini en az 10 olacak sekilde girin.")

        else:
            break
    puan = 0
    for i in range(boyut):
        oyun_alani.append(["?"]*boyut)

    def oyunAlaniYazma(oyun_alani):
        for satir in oyun_alani:
            print(" ".join(satir))

    def rastgeleHucre(oyun_alani):
        return random.randint(0,len(oyun_alani)-1)

    mayin_boyut = boyut*boyut*30//100

    for i in range(mayin_boyut):
        mayin += [[rastgeleHucre(oyun_alani),rastgeleHucre(oyun_alani)]]

    for i in mayin:
        if mayin.count(i) > 1:
            mayin.remove(i)
            mayin.append([rastgeleHucre(oyun_alani),rastgeleHucre(oyun_alani)])
        else:
            continue

    metod = input("Oyunu oynamak istediginiz metodu seciniz\n1 = Acik Mod\n2 = Gizli Mod\nSecim ->")

    def acikMod():
        for i in mayin:
            oyun_alani[i[0]][i[1]] = "X"
        return oyunAlaniYazma(oyun_alani)

    if metod == "1":
        print(acikMod())

    elif metod == "2":
        oyunAlaniYazma(oyun_alani)

        while True:
            mayinSayisi = 0
            satir = int(input("Satir degerini giriniz:"))
            sutun = int(input("Sutun degerini giriniz:"))

            secim = [satir, sutun]

            if secim in mayin:
                if oyun_alani[satir-1][sutun-1] in secim:
                    print("Zaten Tahmin ettiniz.")
                    oyunAlaniYazma(oyun_alani)
                else:
                    oyun_alani[satir - 1][sutun - 1] = "X"
                    print("Maalesef kaybettiniz.",acikMod())
                    break

            else:
                if secim[0] < 0 or secim[1] < 0 or secim[0] > boyut or secim[1] > boyut:
                    print("Oyun dısı alanda tahminde bulundunuz.")
                else:
                    if [satir,sutun-1] in mayin:
                        mayinSayisi += 1
                    if [satir-1,sutun-1] in mayin:
                        mayinSayisi += 1
                    if [satir-1,sutun] in mayin:
                        mayinSayisi += 1
                    if [satir-1,sutun+1] in mayin:
                        mayinSayisi += 1
                    if [satir,sutun+1] in mayin:
                        mayinSayisi += 1
                    if [satir+1,sutun+1] in mayin:
                        mayinSayisi += 1
                    if [satir+1,sutun] in mayin:
                        mayinSayisi += 1
                    if [satir+1,sutun-1] in mayin:
                        mayinSayisi += 1
                    oyun_alani[satir - 1][sutun - 1] = str(mayinSayisi)
                    oyunAlaniYazma(oyun_alani)
                    puan += 1

            if puan == int((boyut*boyut*70)//100):
                print("Oyunu kazandiniz.Puaniniz ->{}".format(puan))
                break

    else:
        print("Lutfen belirtilen secimlerden birini tercih edin.")