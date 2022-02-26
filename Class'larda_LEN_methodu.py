class Fruits():
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __len__(self):
        return 2

my_fruit = Fruits("Banana",200)
print("uzunluk",len(my_fruit))