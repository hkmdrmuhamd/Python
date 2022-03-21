class Kisi:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

class Ogrenci(Kisi):
    def __init__(self,sinif,aldigi_ders_sayisi):
        self.sinif = sinif
        self.aldigi_ders_sayisi = aldigi_ders_sayisi

    def yazdir(self):
        print(self.ad,self.soyad,int(self.yas),int(self.sinif),int(self.aldigi_ders_sayisi))

class Ogretmen(Kisi):
    def __init__(self,unvan,maas):
        self.unvan = unvan
        self.maas = maas

    def Yazdir(self):
        print(self.ad,self.soyad,int(self.yas),self.unvan,int(self.maas))

ogrenci = Ogrenci(None,None)
ogrenci.ad = input("Ad:")
ogrenci.soyad = input("Soyad:")
ogrenci.yas = int(input("Yas:"))
ogrenci.sinif = int(input("Sinif:"))
ogrenci.aldigi_ders_sayisi = int(input("Aldigi ders sayisi"))
ogrenci.yazdir()

ogretmen = Ogretmen(None,None)
ogretmen.ad = input("Ad:")
ogretmen.soyad = input("Soyad:")
ogretmen.yas = int(input("Yas:"))
ogretmen.unvan = input("Unvan")
ogretmen.maas = int(input("Maas"))
ogretmen.Yazdir()