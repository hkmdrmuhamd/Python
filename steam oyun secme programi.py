""""
Kart Numaralari:
Paypal = 123
Master Card = 456
Visa = 789
"""

oyunlar = ['Cs-Go' , "Gta-5" , "Cyberpunk 2077" , "Apex Legend"]
odeme_yontemi = ["Paypal" , "Master Card" , "Visa"]
oyun = str(input("Hangi oyunu almak istersiniz? ->"))

i = j = 0

if oyun == oyunlar[i]:
    versiyon = int(input("Hangi versiyonu yuklemek istiyorsunuz:"))
    if versiyon == 1:
        print("Bu versiyon ucretsizdir indirmeniz baslatiliyor..")

    elif versiyon == 2:
        print("Bu versiyonda bazi ozel modlar acik oldugu icin odeyeceginiz tutar: '24TL'")
        input("Sizi oyunu satin alma ekranina yonlendiriyorum lutfen devam et butonuna basiniz.")

    elif versiyon == 3:
        print("Bu versiyonda bazi modlarla beraber silah desenleri de aciktir bu sebeple odeyecegini tutar: '45TL'")
        input("Sizi oyunu satin alma ekranina yonlendiriyorum lutfen devam et butonuna basiniz.")

elif oyun == oyunlar[i+1]:
    print("Bu oyun 150TL'dir.")
    input("Sizi oyunu satin alma ekranina yonlendiriyorum lutfen devam et butonuna basiniz.")

elif oyun == oyunlar[i+2]:
    print("Bu oyun 275TL'dir.")

elif oyun == oyunlar[i+3]:
    print("Bu oyunu satin alabilmeniz icin 'EA play' magazasini da indirmeniz gerekmektedir.")
    input("Indirme islemini baslatmak icin devam et butonuna basiniz ->")
    print("Indirme islemi baslatilmistir...")
    input("Indirme islemi tamamlanmistir. Sizi oyunu satin alma ekranina yonlendiriyorum lutfen devam et butonuna basiniz.")

    odeme = str(input("Hangi kartla odeme yapmak istiyorsunuz: "))

    if odeme == odeme_yontemi[j]:
       print("Kart numaranizi giriniz:\n")
       no = int(input())

       print("Lutfen kart sifrenizi giriniz:\n")
       sifre = input()

       if no != 123:
         print("Kart numarasi ile sifre uyusmamaktadir.")

       else:
          print("Satin alim basarili..")

    elif odeme == odeme_yontemi[j+1]:
       print("Kart numaranizi giriniz:")
       no = int(input())

       print("Lutfen kart sifrenizi giriniz:")
       sifre = input()

       if no != 456:
          print("Kart numarasi ile sifre uyusmamaktadir.")

       else:
          print("Satin alim basarili..")

    elif odeme == odeme_yontemi[j+2]:
       print("Kart numaranizi giriniz:")
       no = int(input())

       print("Lutfen kart sifrenizi giriniz:")
       sifre = input()

       if no != 789:
          print("Kart numarasi ile sifre uyusmamaktadir.")

       else:
          print("Satin alim basarili..")

    else:
       print("Bu kartla yapılacak odemeyi sistemimiz kabul etmemektedir.")

else:
    print("Oyle bir oyun bulunamadi. Oyunun adini yanlis girmediginizden emin olun.")