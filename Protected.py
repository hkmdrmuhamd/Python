class Company:
    def __init__(self,project):
        self._project = 'NLP'

class Employee(Company):
    def __init__(self,name,project):
        self.name = name
        super().__init__(project)
    def show(self):
        print("Employee name:",self.name)
        print("working on project:",self._project) #Hem farkli bir class icinden erisim saglandi

c = Employee("x",None)
c.show()
print("Project:",c._project) # Hem de disardan erisim saglanabildi