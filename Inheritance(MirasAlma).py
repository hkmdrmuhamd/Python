class Class1():
    def __init__(self):
        print("Class 1 created")

    def method_1(self):
        print("method 1")

    def method_2(self):
        print("method 2")

my_example = Class1()
#my_example.method_1()
#my_example.method_2()

class Class2(Class1):
    def __init__(self):
        Class1.__init__(self)
        print("Class 2 created")

    def method_3(self):
        print("method 3")

my_example2 = Class2()
my_example2.method_1()
my_example2.method_3() #bu method sadece class 2 de var class 1 de cagiramayiz