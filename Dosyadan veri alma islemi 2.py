with open("Dosyadan veri alma ve okuma islemleri.txt","r") as dosya: #Dosya ile ilgili islemi yaptıktan sonra dosyayı kapatir
    dosya.seek(10) #Dosyada 10 harf sonrasindaki veriyi ekrana basar
    print(dosya.read())
    dosya.seek(5) #Tekrar yazdirirsak en bastan baslar yine 5 harf sonrasini basar yani kaldigi yerde devam etmez
    print(dosya.read(6)) #read icine sayi yazarsak ilk 5 harften sonra gelen 6 harfi yazdirir gersini yazdirmaz
    dosya.close()