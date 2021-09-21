def ortalama(sayi1,sayi2):

    topla = i = ort = adet = 0

    for i in range((sayi1+1),(sayi2-1)):
        if i % 2 == 0:
            topla += i
            adet+=1
    i+=1

    ort = topla / adet

    return ort

sayi1 = int(input("Birinci sayiyi giriniz ->"))

sayi2 = int(input("Ikinci sayiyi giriniz ->"))

print("Girdiginiz sayilarin arasindaki cift degerlerin ortalamasi: {}".format(ortalama(sayi1,sayi2)))
