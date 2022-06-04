class Book:
    def __init__(self,baslik,miktar,yazar,fiyat):
        self.baslik = baslik
        self.miktar = miktar
        self.yazar = yazar
        self.__fiyat = fiyat
        self.__discount = None

    def set_discount(self,discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__fiyat*(self.__discount)
        return self.__fiyat

    def print(self):
        return f"Kitap = {self.baslik},Miktar = {self.miktar},Yazar = {self.yazar},Fiyat = {self.get_price()}"

obj1 = Book("abc",1,"zxc",300)
obj2 = Book("def",2,"qwe",500)

print(obj1.print())
print(obj2.print())
obj2.set_discount(0.2)
print(obj2.print())