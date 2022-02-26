class DogYears:
    default_age = 7
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.age_hesaplama = age * self.default_age

    def yasHesapla(self):
        return self.age * 7

age = int(input("Kopeginiz kac yasinda:"))
name = str(input("Kopeginizin ismi nedir:"))
dog = DogYears(name,age)
print(f"{dog.name} insan yilina gore yasi:",dog.yasHesapla())
print(dog.age_hesaplama)