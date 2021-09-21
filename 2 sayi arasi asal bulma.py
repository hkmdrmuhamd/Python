def asalBulma(sayi1,sayi2):
    for i in range(sayi1+1,sayi2+1):
        if i > 1:
            for j in range(2,i):
              if i % j == 0:
                  break
            else:
                print("{} asaldir.".format(i))

sayi1 = int(input("Baslangic sayisini giriniz:"))
sayi2 = int(input("Bitis sayisini giriniz:"))


asalBulma(sayi1,sayi2)