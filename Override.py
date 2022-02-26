class Class1():
    def __init__(self):
        print("Class 1 created")

    def method_1(self):
        print("method 1")

    def method_2(self):
        print("method 2")

#my_example = Class1()

class Class2(Class1):
    def __init__(self):
        Class1.__init__(self)
        print("Class 2 created")

    def method_3(self):
        print("method 3")

                             #OVERRİDE
    def method_1(self):
        print("method 1 override edildi")

my_example2 = Class2()
my_example2.method_1()