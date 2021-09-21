def asal_sayi(sayi):

    sayac = 2

    while sayac * sayac < sayi:
        if sayi % sayac == 0:
            return False
        sayac += 1
    else:
        return True

sayi = int(input("Bir sayi giriniz:"))

print("Girdiginiz sayi asaldir -> {}".format(asal_sayi(sayi)))