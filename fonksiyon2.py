def geometrik_sekil_bulucu3(kenar1,kenar2 ,kenar3 ,kenarSayisi):
        if kenar1 < (kenar2+kenar3) and kenar2 < (kenar1+kenar3) and kenar3 < (kenar2+kenar1):
           if kenar1 == kenar2 == kenar3:
               print("Eskenar ucgen olusturdunuz.")

           elif kenar1==kenar2 or kenar2==kenar3 or kenar1==kenar3:
               print("Ikiz kenar ucgen olusturdunuz.")

           else:
               print("Ucgen olusturdunuz.")

        else:
           print("Girdiginiz degerlerle bir ucgen olusturulamiyor.")

def geometrik_sekil_olusturucu4(kenar1,kenar2,kenar3,kenar4,kenarSayisi):
    if kenar1 == kenar2 == kenar3 == kenar4:
        print("Kare olusturdunuz.")

    elif kenar1 == kenar2 and kenar3 == kenar4:
        print("Dikdortgen olusturdunuz.")

    else:
        print("Dortgen olusturdunuz.")

kenarSayisi = int(input("Kac kenarli bir sekil olusturmak istiyorsunuz (min = 3 - max = 4) ->"))

if kenarSayisi == 3:
    kenar1 = input("Kenar 1 ->")
    kenar2 = input("Kenar 2 ->")
    kenar3 = input("Kenar 3 ->")
    geometrik_sekil_bulucu3(kenar1, kenar2, kenar3,kenarSayisi)

elif kenarSayisi == 4:
    kenar1 = input("Kenar 1 ->")
    kenar2 = input("Kenar 2 ->")
    kenar3 = input("Kenar 3 ->")
    kenar4 = input("Kenar 4 ->")
    geometrik_sekil_olusturucu4(kenar1, kenar2, kenar3, kenar4, kenarSayisi)