sozluk = dict()

key_sayisi = int(input("Kac key degeri girmek istiyorsunuz:"))

for i in range(1,key_sayisi+1):
    key = input("{}. key degerini giriniz:".format(i))
    values = input("{}. values degerini giriniz:".format(i))
    sozluk.update({key:values})
print(sozluk)