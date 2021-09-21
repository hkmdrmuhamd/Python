def daireAlani(yarim):
    Alan = (yarim**2)*3.14
    return Alan

yaricap = int(input("Dairenin yaricapini giriniz:"))

print("Dairenin alani -> {}".format(daireAlani(yaricap)))

def cevre(pi,r):
    Cevre = 2*pi*r
    return Cevre

print(cevre(3.14,2))