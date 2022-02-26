class Fruits():
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name} has {self.calories} calories"

my_fruit = Fruits("Banana",200)
#str method'umuzu yazmasaydik print(my_fruit) yazinca bize bir adres degeri verirdi
print(my_fruit)
