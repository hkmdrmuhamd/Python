"""class Bird:
    def into(self):
        print("There are any type of bird")
    def flight(self):
        print("Most of the birds can fly")

class sparrow(Bird):
    def flight(self):
        print("sparrow can fly")

class ostrich(Bird):
    def flight(self):
        print("ostrich can't fly")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
obj_spr.into()
obj_spr.flight()#Override islemi gerceklesti(sparrow icindeki printi aldi)
obj_ost.into()
obj_ost.flight()#Override islemi gerceklesti(ostrich icindeki printi aldi)
obj_bird.flight()"""

"""class vehicle:
    def max_speed(self):
        print("max speed is 100")

class Car(vehicle):
    def max_speed(self):
        print("Max speed is 200")

car_obj = Car()
car_obj.max_speed()"""

class message:
    def detalis(self,phrase = None):
        if phrase is not  None:
            print("Mesaj"+phrase)
        else:
            print("Merhaba")

obj = message()
obj.detalis()