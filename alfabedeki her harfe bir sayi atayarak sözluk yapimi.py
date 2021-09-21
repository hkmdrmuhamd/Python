"""harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
sozluk = {}

for i in harfler:
    sozluk[i] = harfler.index(i)

print(sozluk)"""

#listedeki kelimelerin uzunlugunu bulup bunu sozluk seklinde yazdiran program
"""isimler = ["muhammed","ahmet","ayse","yaren","merve"]
sozluk = {}
a = 0
for i in isimler:
    for j in i:
        a += 1
    sozluk[i] = a
    a = 0
print(sozluk")"""

"""isimler = ["muhammed","ahmet","ayse","yaren","merve"]  #satır 9 daki kod ile aynı işlevi görür
sozluk = {i : len(i) for i in isimler}
print(sozluk)"""
#Girilen bir değere kadar olan sayıları anahtar olarak tutup bu sayıların karesini alıp values değerlerine eşitleme
"""sozluk = {}
i = 1
n = int(input("Bir deger giriniz:"))
while i < len(range(0,n)):
    b = i*i
    sozluk.update({i:b})
    i += 1
print(sozluk)"""