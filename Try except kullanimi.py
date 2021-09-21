sayi1 = input("Bir sayi giriniz:")
sayi2 = input("Bir sayi giriniz:")

try:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1/sayi2)

except ValueError: #Eger degerlerden biri string bir ifade girilirse ValueError hatasi verir
    print("String bir ifade girdiniz.Lütfen sayi giriniz.")

except ZeroDivisionError:  #Eger 2. sayi sifir girilmisse sayi bolu sıfır = tanimsiz oldugundan ZeroDivisionError hatasi verir
    print("Sayı sıfıra bölünemez.Lütfen 2. sayı için sıfır dışında bir değer giriniz.")

#Bu hatalar tek bir except blogunda da yazilabilir
"""try:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1 / sayi2)

except(ValueError,ZeroDivisionError):
    print("Bir hata olustu")"""