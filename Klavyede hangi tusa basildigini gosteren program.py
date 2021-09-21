harfler = ['q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','i','z','x','c','v','b','n','m']

sayilar = ['1','2','3','4','5','6','7','8','9','0']

semboller = [' ','"','/','*','+','-',',','.']


tus = str(input("Herhangi bir tusa basiniz:"))
if tus in harfler:
     print("Bastiginiz tus: {}".format(tus))

elif tus in sayilar:
     print("Bastiginiz tus: {}".format(tus))

elif tus in semboller:
     if tus == ' ':
        print("Bastiginiz tus: space")
     else:
        print("Bastiginiz tus: {}".format(tus))
