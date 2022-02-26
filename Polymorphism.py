class Apple:
    def __init__(self,name):
        self.name = name

    def information(self):
        return self.name + " 100 calories"

class Banana:
    def __init__(self,name):
        self.name = name

    def information(self):
        return self.name + " 200 calories"

banana = Banana("muz")
apple = Apple("elma")
#banana.information()
#apple.information()

fruit_list = [banana,apple]

for fruit in fruit_list: #tek bir degisken ile(fruit) her iki sinifin da bilgi methoduna erisim sagradik
    print(fruit.information())