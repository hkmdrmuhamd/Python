print("\n---------------THE WALKING DEAD SIMULASYON OYUNUNA HOSGELDINIZ---------------\n")

input("Oyuna kayit olmak icin devam et tusuna basiniz ->")

e_posta = str(input("Bir e posta hesabi giriniz: "))

sifre = str(input("Bir sifre belirleyiniz: "))

sifre_tekrar = str(input("Sifrenizi tekrar giriniz: "))

if sifre == sifre_tekrar:
    input("Sizi giris ekranina yonlendiriyorum...\nLutfen devam et tusuna basiniz ->")

    print("\n")

    girisE = input("e posta adresinizi giriniz:")

    giriS = input("sifrenizi giriniz:")

    if girisE == e_posta:
        if giriS == sifre:
            print("Tebrikler giris basarili...")
        else:
            print("Sifrenizi yanlis girdiniz lutfen sifrenizi dogru giriniz.")
    else:
        print("e posta adresiniz yanlis lutfen kontrol edip tekrar deneyiniz.")
else:
    print("Ilk girdiginiz sifreyle ikincisi uyusmuyor lutfen kontrol ediniz.")