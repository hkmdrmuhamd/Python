def asal_carpan(sayi):
    sayac = 2
    temp = 0

    while sayac < sayi:
        if sayi % sayac == 0:
            temp = sayac
            print("Asal carpanlar: ",temp)

        sayac += 1

    if temp == 0:
        print("Girdiginiz sayi asaldir.")


sayi = int(input("Bir sayi degeri giriniz ->"))
asal_carpan(sayi)
