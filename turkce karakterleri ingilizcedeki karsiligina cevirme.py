harfler = {"ı":"i","ö":"o","ü":"u","ğ":"g","ş":"s","ç":"c","İ":"I","Ü":"U","Ö":"O","Ğ":"G","Ş":"S","Ç":"C"}

kelime = input("Bir kelime giriniz:")
tr_kelime = "ığüşöçĞÜŞİÖÇ"
ing_kelime = ""
for i in kelime:
    if i in tr_kelime:
        ing_kelime += harfler[i]
    else:
        ing_kelime += i

print(ing_kelime)