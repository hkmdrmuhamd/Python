class A:
    def __init__(self,hobi1):
        self.hobi1 = hobi1

class B(A):
    def __init__(self,hobi1,hobi2):
        super().__init__(hobi1)
        self.hobi2 = hobi2

class C(B):
    def __init__(self,hobi1,hobi2,hobi3):
        super().__init__(hobi1,hobi2)
        self.hobi3 = hobi3
    def Yazdir(self):
        print(hobi1,hobi2,self.hobi3)

hobi1 = input("Hobi 1:")
hobi2 = input("Hobi 2:")
hobi3 = input("Hobi 3:")
obj1 = A(hobi1)
obj2 = B(None,hobi2)
obj3 = C(None,None,hobi3)
obj3.Yazdir()