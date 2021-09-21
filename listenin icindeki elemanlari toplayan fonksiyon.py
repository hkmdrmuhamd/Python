def topla(liste):
    toplam = 0
    i = 0
    for i in range(len(liste)):
        toplam += liste[i]
        i+=1
    return toplam

liste = [1,2,3,4,5,6]

print("Listenin toplami:{}".format(topla(liste)))

