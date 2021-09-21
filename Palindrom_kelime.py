#Kullanicidan alinan kelimenin palindrom olup olmadigini bulan program
liste = []
newliste = []

kelime = str(input("Bir kelime giriniz:"))

for i in kelime:
    liste += [i]

i = 1

while i <= len(liste):
    newliste += liste[-i]
    i += 1

if liste == newliste:
    print("Girdiginiz kelime palindrom bir kelimedir.")

else:
    print("Girdiginiz kelime palindrom bir kelime değildir.")