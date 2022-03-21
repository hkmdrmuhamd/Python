class Car1:
    def __init__(self,marka,renk,motor_hacmi):
        self.marka = marka
        self.renk = renk
        self.motor_hacmi = motor_hacmi

class Car2(Car1):
    def __init__(self,marka,renk,motor_hacmi,yakit_turu):
        super().__init__(marka,renk,motor_hacmi)
        self.yakit_turu = yakit_turu
    def yazdir(self):
        print(self.marka,self.renk,self.motor_hacmi,self.yakit_turu)

marka = input("Marka:")
renk = input("Renk:")
motor_hacmi = input("Motor hacmi:")
yakit_turu = input("Yakit turu:")

obj = Car2(marka,renk,motor_hacmi,yakit_turu)
obj.yazdir()