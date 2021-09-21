"""with open("Dosyalarda Degisiklik Yapmak.txt","a") as dosya:
    dosya.write("Okudugu bolum = Bilgisayar Muhendisligi") #Bu islemi dosyanin en sonuna ekler

with open("Dosyalarda Degisiklik Yapmak.txt","r+") as dosya: #r+ = Dosyayi hem okumayi hem de dosyaya yazmayi saglar
    veriler = dosya.read() #Dosyadaki tum verileri veriler degiskenine atadik
    dosya.seek(0)  #Dosyanin en basina gittik
    veriler = "Hobileri = Bilgisayar Oyunlari" + veriler #Veriler degiskenine yeni bir veri ekledik bu sayede en basa ekleme yapmıs olduk
    dosya.write(veriler) #Son olarak ekledigimiz veriyi dosyamiza yazdirdik"""

with open("Dosyalarda Degisiklik Yapmak.txt","r+") as dosya:
    veriler = dosya.readlines() #Dosyadaki verileri liste seklinde aldik
    veriler.insert(1,"En sevdigi oyun = The Witcher Serisi") #insert = Dosyada ara kisimlara veri eklememizi saglar burda 1,veriden
                                                             #sonra yeni bir veri ekleme islemi yaptik
    dosya.seek(0) #Dosyanin en basina geldik
    dosya.writelines(veriler) #Yeni ekledigimiz veriyi dosyamiza yazdiriyoruz
    dosya.close()