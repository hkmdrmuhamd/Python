class Ad:
    def __init__(self,ad):
        self.ad = ad

class soyad:
    def __init__(self,soyad):
        self.soyad = soyad

class Kisi(Ad,soyad):
    def __init__(self,ad,soyad,yas):
        super().__init__(ad)
        super().__init__(soyad)
        self.yas = yas

    def Yazdir(self):
        print(self.ad,self.soyad,int(self.yas))

obj = Kisi(None,None,None)
isim = input("Ad:")
soyisim = input("Soyad:")
Yas = int(input("Yas:"))
obj.ad = isim
obj.soyad = soyisim
obj.yas = Yas
obj.Yazdir()

