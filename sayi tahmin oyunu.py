import random

sayi = random.randint(1,50)

hak = 5
print("Oyunumuzda 1 ile 50 arasinda rastgele bir sayi belirlenmistir.Sayiyi dogru tahmin etmeniz icin 5 hakkiniz vardir. Basarilar..")

while hak > 0:
    tahmin = int(input("Bir tahminde bulunun:"))

    if tahmin == sayi:
        print("Dogru tahmin ettiniz.Puaniniz ={}".format(hak*2))
        break

    elif tahmin < sayi:
        print("Daha yuksek bir deger giriniz.")
        hak -= 1

    elif tahmin > sayi:
        print("Daha kucuk bir deger giriniz:")
        hak -= 1

else:
    print("Tum haklarinizi kullandiniz. Farkli bir deger giremezsiniz.")