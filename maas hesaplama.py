maas = float(input("Maas bilginizi giriniz:"))
gelir = str(input("Maasiniz haricinde ek geliriniz var mi 'E' ya da 'H' ->"))
ssk = str(input("SSK'nız var mı 'E' ya da 'H':"))

if gelir == 'E' and ssk == 'E':
    ekGelir = float(input("Ek gelir tutarinizi giriniz:"))
    maas += ekGelir
    kesinti = maas - ((maas * 12)/100)
    BrutMaas = kesinti - ((kesinti * 15)/100)
    print("Brut maasiniz -> {}".format(BrutMaas))

elif gelir == 'E':
    ekGelir = float(input("Ek gelir tutarinizi giriniz:"))
    maas += ekGelir
    BrutMaas = maas - ((maas * 12) / 100)
    print("Brut maasiniz -> {}".format(BrutMaas))

elif ssk == 'E':
    BrutMaas = maas - ((maas * 15) / 100)
    print("Brut maasiniz -> {}".format(BrutMaas))

else:
    print("Brut maasiniz -> {}".format(maas))