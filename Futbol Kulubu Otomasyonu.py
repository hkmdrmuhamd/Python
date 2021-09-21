                                     #Muhammed Hukumdar - 20010011067

bilgiler = dict()     #Butun futbolcu bilgilerinin bulundugu genel sozlugumuz belirlenmistir
dosya = open("20010011067.txt","w+")  #Gerekli bilgileri kaydetmek icin dosya adinda bir metin dosyasi acilmistir
dosya.write("               Muhammed Hukumdar - 20010011067\n\n")   #Dosyaya adimi soyadimi ve numarami yazdirdim

def secim(deger):    #Bu fonksiyonun amaci menudeki secim degerlerini algilayip kullanisli bir menu tasarimi yapmaktir
    if deger == 1:
        ekleme()
    elif deger == 2:
        silme()
    elif deger == 3:
        arama()
    elif deger == 4:
        bilgi_guncelleme()
    elif deger == 5:
        sozlesme()
    elif deger == 6:
        prim()
    elif deger == 7:
        bilgi()

def ekleme():           #Ekleme fonksiyonu ile futbolcu bilgileri kullanicidan alinip sisteme eklenir
    futbolcu_id = 1     #istenilen futbolcu bilgisini alabilmek icin her futbolcuya bir id numarasi belirlendi
    futbolcu_sayisi = int(input("Kac adet futbolcu eklemek istersiniz:"))
    for i in range(1, futbolcu_sayisi + 1):
        futbolcu_bilgisi = dict()    #Futbolcularin bilgilerinin karismamasi icin girilen bilgiler bir sozluk olarak kaydedildi
        adSoyad = input("{}. Futbolcunun adi soyadi nedir -> ".format(i))
        futbolcu_bilgisi["Ad-Soyad"] = adSoyad   #Belirledigimiz sozluge key degerlerini verip kullanicidan bunlarin karsiligi alinarak sozluge eklenir
        dosya.write(adSoyad)         #Girilen bilgiler daha once actigimiz dosyamiza kaydedilir
        dosya.write("\n")
        maas = int(input("{}. futbolcuya ait maas bilgisini giriniz ->".format(i)))
        futbolcu_bilgisi["Maas"] = maas
        dosya.write(str(maas))
        dosya.write("\n")
        forma_no = int(input("{}. futbolcuya ait forma numarasini giriniz ->".format(i)))
        futbolcu_bilgisi["Forma No"] = forma_no
        dosya.write(str(forma_no))
        dosya.write("\n")
        bilgiler[futbolcu_id] = futbolcu_bilgisi    #Bu islem ile futbolcu bilgilerinin bulundugu sozlugumuz genel bilgilerin bulundugu sozluge eklenir
        futbolcu_id += 1

def silme():    #Futbolcunun kimlik bilgisi olan id ile kayitli futbolculardan istedigimizi silebiliriz
    futbolcu_id = int(input("Hangi futbolcuya ait bilgileri silmek istersiniz.(Futbolcunun ID'sini giriniz):"))
    if futbolcu_id in bilgiler.keys():
        del bilgiler[futbolcu_id]
        print("{} numarali ID'ye sahip futbolcu bilgileri silinmistir menuden 7 rakamini tuslayarak kayitli listeden bakabilirsiniz.".format(futbolcu_id))

    else:
        print("Girdiginiz ID'de futbolcu bulunamadi")

def arama():   #Bu fonksiyon ile istenilen futbolcunun guncel bilgilerine erisilebilir
    ID = int(input("Hangi ID sahip futbolcunun bilgilerini yazdirmak istiyorsunuz:"))
    if ID in bilgiler.keys():
        for futbolcu_bilgisi in bilgiler[ID].keys():
            print("{} : {}".format(futbolcu_bilgisi, bilgiler[ID][futbolcu_bilgisi]))
    else:
        print("Girdiginiz ID sahip futbolcu bulunamadi.")

def bilgi_guncelleme():   #Bu fonksiyon ile futbolcunun bilgilerinde degisiklik yapilabilir
    Key = input("Futbolcunun kayitli hangi bilgisini guncellemek istiyorsunuz.(Key degeridir eksiksiz giriniz!!):")
    ID = int(input("Hangi id'deki futbolcunun {} adli bilgisini guncellemek istiyorsunuz:".format(Key)))
    if ID in bilgiler.keys():
        for futbolcu_id in bilgiler.keys():   #Sozlugun key degerlerinde tek tek arama yaparak girilen id bulunur
            if futbolcu_id == ID:
                bilgiler[futbolcu_id][Key] = input("Lutfen guncel {} bilgisini giriniz:".format(Key))

        for futbolcu_bilgisi in bilgiler[ID].keys():
                print("{} : {}".format(futbolcu_bilgisi, bilgiler[ID][futbolcu_bilgisi]))
    else:
        print("Girdiginiz ID sahip futbolcu bulunamadi.")

def sozlesme():   #Futbolcunun sozlesmesiyle ilgili bir anlasma yapildiginda istege bagli olarak bu bilgi girilebilir
    ID = int(input("Hangi ID sahip futbolcunun sozlesmesini ayarlamak istiyorsunuz:"))
    if ID in bilgiler.keys():
        sozluk = bilgiler[ID]   #Futbolcunun kayitli bilgilerinin bulundugu sozluge erismek icin bu istem yapilmistir
        Sozlesme = int(input("{}. ID'deki futbolcuya ait sozlesme kac yillik:".format(ID)))
        for fut_id in bilgiler.keys():
            if fut_id == ID:
                sozluk.update({"Sozlesme":Sozlesme}) #Istege bagli oldugundan bu bilgi girilmek istenirse guncel bilgiler arasina sozlesme bilgisi eklenir

        for fut_bilgi in bilgiler[ID].keys():
            print("{} -> {}".format(fut_bilgi, bilgiler[ID][fut_bilgi]))

    else:
        print("Boyle bir ID bulunamadi.")

def prim(): #Bu fonksiyon da futbolcunun gosterdigi performans sonrasi girilen bilgileri tutar
    ID = int(input("Hangi ID'deki futbolcuya prim vermek istiyorsunuz:"))  #Futbolcunun attigi gol sayisina gore verilecek prim miktari hesaplanir
    if ID in bilgiler.keys():
        sozluk = bilgiler[ID]   #Futbolcunun kayitli bilgilerinin bulundugu sozluge erismek icin bu istem yapilmistir
        for fut_id in bilgiler.keys():
            liste = list()  #Futbolcunun prim-gol sayisini ayni anda tutmak icin bir liste olusturulmustur
            if fut_id == ID:
                golSayisi = int(input("{}. ID'deki futbolcunun attigi gol sayisi kactir:".format(ID)))
                Prim = golSayisi + (golSayisi * 40) #Bu islem futbocunun attigi gol sayisina, gol sayisinin 40 katini ekleyip verilecek prim miktarini belirler
                print("Atilan gol sayisina gore futbolcuya odenecek prim miktari : {}".format(Prim))
                liste.append(golSayisi)   #Listeye gol ve prim miktari eklendi
                liste.append(Prim)
                sozluk.update({"Gol-Prim": liste})   #Gol-prim bilgisinin yer aldigi liste sozluge eklendi

        for fut_bilgi in bilgiler[ID].keys():
            print("{} -> {}".format(fut_bilgi, bilgiler[ID][fut_bilgi]))

    else:
        print("Boyle bir ID bulunamadi.")

def bilgi():   #Sistemde kayitli olan futbolcularin bilgilerini goruntulemek icin kullanilir
    print(bilgiler)

def main():  #Menunun bulundugu fonksiyondur bu fonksiyon ile menu kullaniciya sunulur
    print("\n")
    print("---------------FUTBOLCU BİLGİLERİ MENUSU---------------")
    print("[1]:Futbolcu Ekleme")
    print("[2]:Futbolcu Silme")
    print("[3]:Futbolcu Arama")
    print("[4]:Futbolcu Bilgi Guncelleme")
    print("[5]:Futbolcu Sozlesme Suresi")
    print("[6]:Futbolcuya Odenecek Prim Miktari")
    print("[7]:Sistemde Kayitli Tum Futbolcularin Bilgileri")
    print("[8]:Cikis")
    print("-------------------------------------------------------")
    while True:  #Kullanici cikis yapmayana kadar sonsuz bir dongu olusturulmustur
        deger = int(input("\nLütfen menuden yapmak istediginiz islemi secin :"))
        if deger == 8:  #Eger kullanici 8 degerini girerse menuden cikis yapilir
            break
        else:
            secim(deger)
main()  #Tum bu islemlerin hepsi tek bir main fonksiyonu ustunden gerceklestirilmistir