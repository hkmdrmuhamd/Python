class A:
    def __init__(self,kredi):
        self.kredi = kredi

class B(A):
    def __init__(self,silah):
        super().__init__(kredi)
        self.silah = silah

class C:
    def __init__(self,yetenek):
        self.yetenek = yetenek

class D(B,C):
    def __init__(self,desen):
        super().__init__(silah)
        super().__init__(yetenek)
        self.desen = desen
    def Yazdir(self):
        print("Silah:"+silah,"\nKredi:"+kredi,"\nYetenek:"+yetenek,"\nDesen:"+self.desen)

kredi = input("Kredi:")
silah = input("Silah:")
desen = input("Desen:")
yetenek = input("Yetenek:")
objA = A(kredi)
objB = B(silah)
objC = C(yetenek)
objD = D(desen)
objD.Yazdir()