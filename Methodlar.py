class Musician:
    job = "musician" #deafult degerdir sonradan değiştirilebilir
    def __init__(self,name,age,instrument):
        self.name = name
        self.age = age
        self.instrument = instrument

    #METHOD
    def sing(self):
        print(f"We are the champions! {self.name}")

my_musician = Musician("James",50,"Guitar")

print(my_musician.name,my_musician.age,my_musician.instrument,my_musician.job)

my_musician.job = "singer"#goruldugu gibi sonradan bu deger degistirilebildi

my_musician.sing()