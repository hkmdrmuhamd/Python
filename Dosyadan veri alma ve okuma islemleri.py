dosya = open("Dosyadan veri alma ve okuma islemleri.txt","r")

"""print(dosya.read()) Dosyadaki tum verileri ekrana yazdirir

print(dosya.readline()) Dosyadaki verileri tek tek satir satir yazdidir

print(dosya.readlines())  Dosyadaki tüm verileri liste seklinde ekrana basar"""

#print(dosya.read())
#print(dosya.readline())
#print(dosya.readlines())

liste = dosya.readlines()

print(liste[2])

dosya.close() #Dosyayı kapatmayı saglar