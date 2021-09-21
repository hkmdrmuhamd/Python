                                    #Muhammed Hukumdar 20010011067

def secim(deger):
    if deger == 1:
        toplama()
    elif deger == 2:
        cikarma()
    elif deger == 3:
        carpma()
    elif deger == 4:
        bolme()
    elif deger == 5:
        kareAlma()


def toplama():
    dosya = open("20010011067.txt", "a")
    toplam = 0
    dosya.write("Toplama -> ")
    degerSayisi = int(input("Kac adet sayiyi toplamak istiyorsunuz:"))
    for i in range(1,degerSayisi+1):
        deger = int(input("Bir deger giriniz:"))
        if deger < 0:
            deger = str(deger)
            dosya.write("(")
            dosya.write(deger)
            dosya.write(")")
        toplam += deger
        deger = str(deger)
        dosya.write(deger)
        dosya.write("+")
    print("Girdiginiz sayilarin toplami = {}".format(toplam))
    toplam = str(toplam)
    dosya.write("=")
    dosya.write(toplam)
    dosya.write("\n\n")
    dosya.close()

def cikarma():
    dosya = open("20010011067.txt", "a")
    dosya.write("Cikarma -> ")
    deger1 = int(input("Birinci sayiyi giriniz:"))
    deger2 = int(input("Ikinci sayiyi giriniz:"))
    cikarma = deger1 - deger2
    if deger1 < 0:
        deger1 = str(deger1)
        dosya.write("(")
        dosya.write(deger1)
        dosya.write(")")
    else:
        deger1 = str(deger1)
        dosya.write(deger1)
    dosya.write("-")
    if deger2 < 0:
        deger2 = str(deger2)
        dosya.write("(")
        dosya.write(deger2)
        dosya.write(")")
    else:
        deger2 = str(deger2)
        dosya.write(deger2)
    print("Girdiginiz sayilarin farki = {}".format(cikarma))
    dosya.write("=")
    if cikarma < 0:
        cikarma = str(cikarma)
        dosya.write("(")
        dosya.write(cikarma)
        dosya.write(")")
    else:
        cikarma = str(cikarma)
        dosya.write(cikarma)
    dosya.write("\n\n")
    dosya.close()

def carpma():
    dosya = open("20010011067.txt", "a")
    dosya.write("Carpma -> ")
    deger1 = int(input("Birinci sayiyi giriniz:"))
    deger2 = int(input("Ikinci sayiyi giriniz:"))
    carpim = deger1 * deger2
    if deger1 < 0:
        deger1 = str(deger1)
        dosya.write("(")
        dosya.write(deger1)
        dosya.write(")")
    else:
        deger1 = str(deger1)
        dosya.write(deger1)
    if deger1 < 0:
        deger1 = str(deger1)
        dosya.write("(")
        dosya.write(deger1)
        dosya.write(")")
    else:
        deger2 = str(deger2)

    dosya.write(deger2)
    dosya.write("*")
    print("Girdiginiz sayilarin carpimi = {}".format(carpim))
    dosya.write("=")
    carpim = str(carpim)
    dosya.write(carpim)
    dosya.write("\n\n")
    dosya.close()


def bolme():
    dosya = open("20010011067.txt", "a")
    dosya.write("Bolme -> ")
    deger1 = int(input("Birinci sayiyi giriniz:"))
    deger2 = int(input("Ikinci sayiyi giriniz:"))
    sonuc = deger1 / deger2

    if deger2 == 0:
        try:
            bolum = deger1 / deger2

        except ZeroDivisionError:
            print("Bir sayi sifira bolunemez lutfen 2. sayi icin farkli bir deger giriniz.")
    else:
        print("Girdiginiz sayilarin bolumu =",deger1 / deger2)

    deger1 = str(deger1)
    deger2 = str(deger2)
    dosya.write(deger1)
    dosya.write("+")
    dosya.write(deger2)
    dosya.write("=")
    sonuc = str(sonuc)
    dosya.write(sonuc)
    dosya.write("\n\n")
    dosya.close()

def kareAlma():
    dosya = open("20010011067.txt", "a")
    dosya.write("Kare Alma -> ")
    deger = int(input("Lutfen bir sayi giriniz:"))
    kare = deger ** 2
    print("Girdiginiz sayinin karesi = {}".format(kare))
    deger = str(deger)
    dosya.write(deger)
    dosya.write("^2")
    dosya.write("=")
    kare = str(kare)
    dosya.write(kare)
    dosya.write("\n\n")
    dosya.close()

def main():
    print("\n")
    print("---------------HESAP MAKİNESİ---------------")
    print("[1]:Toplama")
    print("[2]:Cikarma")
    print("[3]:Carpma")
    print("[4]:Bolme")
    print("[5]:Kare Alma")
    print("[6]:Cikis")
    print("-------------------------------------------------------")
    while True:
        deger = int(input("\nLütfen menuden yapmak istediginiz islemi secin :"))
        if deger == 6:
            break
        else:
            secim(deger)

main()