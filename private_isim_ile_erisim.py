#Isim cagirma yolu ile private degere erisme

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

emp = Employee("Jesse",1000)
print("Name: {}\nSalary:{}".format(emp.name,emp._Employee__salary))