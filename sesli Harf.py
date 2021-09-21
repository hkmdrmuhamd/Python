sesli_harfler = ["i","o","u","e","a","ı","ö","ü"]
sessiz_harfler = ["b","c","d","e","f","g","h","j","k","l","m","n","p","r","s","t","v","y","z","x","w","ç","ş","ğ"]

sesliler = ""
sessizler = ""

kelime = str(input("Bir kelime giriniz:"))

for i in kelime:
	if i in sesli_harfler:
		if i not in sesliler:
			sesliler += i

	elif i in sessiz_harfler:
		if i not in sessizler:
			sessizler += i

print("Sessiz harfler ->{}".format(sessizler))
print("Sesli harfler ->{}".format(sesliler))