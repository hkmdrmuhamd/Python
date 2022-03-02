import subprocess #Python uzerinden linux komutlarini calistirmak icin bu kutuphane kullanilir
import optparse  #Kullanicidan imput degeri almak icin kullanilir
import re  #Bir metin icindeki degerleri aramamizi saglar

#Kullanicinin internete nasil baglandigi bilgisini almak icin kullanilir
#ornegin eger kullanici kablolu baglaniyorsa eth0 olarak girdi yapmalidir
#verdigimiz argumanlari nereye kaydedecegini belirtmek icin dest komutu kullanilir
#burada kullanicidan alinan bilginin interface icerisine kaydedilmesi belirtilmis
#bir key argument olarak da help komutu verilebilir bu komut ile kullanici bu programin nasil calisacagi hakkinda bilgi alir
def Create_Object():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface",help="Kullanicinin internete nasil baglandigi bilgisini almak icin kullanilir\n Ornegin eger kullanici kablolu baglaniyorsa eth0 olarak girdi yapmalidir")
    parse_object.add_option("-m", "--mac", dest="mac_address",help="Kullanicinin kendi mac adresi ile degistirmek istedigi mac adresi girisi")
    return parse_object.parse_args()

def For_Linux_Code(user_interface,user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"]) #Internet baglantisini keser
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address]) #Mac adresini degistirir
    subprocess.call(["ifconfig", user_interface, "up"]) #Internet baglantisini saglar

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig)) #\w ile ifconfig yazinca gelen ether degerindeki mac adresinin degerini bulur
                                                                   #Bununla kullanicinin girdigi mac degerini karsilastirir ve yazdirir
    if new_mac:
        return new_mac.group(0) #Ikı mac adresi eslesiyorsa ekrana yazdirir.(Group(0) yazmamizin sebebi re kutuphanesi karsilastirdigi degeri string olarak yazdirmaz
                                #Biz bu degeri string olarak yazdirmak icin boyle bir ifade kullaniriz)
    else:
        return None

print("Program calisti!") #program calisirken linux terminalinde hicbir sey gozukmedigi icin komutun caistigini
                          #gostermek icin ekrana programin calistigi bilgisini yazdirir

#Kullanicinin girdigi argumanlar bir tuple deger olarak adreste saklandigi icin bu degerlerden gelen sonuclar tuple olarak tutulmalidir
(user_inputs,arguments) = Create_Object()
print("Girdiginiz interface degeri alindi\nGirdiginiz MAC degeri alindi")
For_Linux_Code(user_inputs.interface,user_inputs.mac_address)
kontrol = control_new_mac(str(user_inputs.interface))

if kontrol == user_inputs.mac_address:
    print("MAC adresi degistirildi ve eslestirildi")
else:
    print("Hata!")