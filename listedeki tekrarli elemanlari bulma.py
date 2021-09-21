liste = [1,5,6,7,8,7,2,5]
kontroList = []
newliste = []

for i in liste:
    if i not in kontroList:
        kontroList += [i]
    else:
        newliste += [i]

print("Listenin icinde tekrar eden sayilar -> {}".format(newliste))

