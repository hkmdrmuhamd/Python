import math

def kokBulma(a,b,c):

    kok1 = kok2 = 0

    delta = (b * b) - (4 * a * c)
    if delta < 0:
        print("Kok yoktur")
    else:
        kok1 = (- b - math.sqrt(delta)) / (2 * a)
        kok2 = (- b + math.sqrt(delta)) / (2 * a)

    return kok1 , kok2

sayi1 = int(input("Bir sayi degeri giriniz:"))

sayi2 = int(input("Bir sayi degeri giriniz:"))

sayi3 = int(input("Bir sayi degeri giriniz:"))

print("Kok 1  ve kok 2 = {} ".format(kokBulma(sayi1,sayi2,sayi3)))