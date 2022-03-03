import scapy.all as scapy #Scapy ag taramasi, agda broadcast vs. gibi islemleri yapmamiza olanak saglar
import optparse #Kullanicidan imput degeri almak icin kullanilir

def Create_Object():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ipaddress",help="Kullanicinin girdigi ip araligini sorgular.\nSorgu yapmak istediginiz ip degerini giriniz ip araligini belirtmek icin araya slash isareti koyunuz")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ipaddress:
        print("IP adresini girilmedi!!")
    return user_input

#ARP = Adres Cozumleme Protokolu ag katmani adreslerinin veri baglantisi katmani adreslerine
#cozumlenmesini saglayan bir telekomunikasyon protokoludur.
# ARP sistemden gelen ip adresinin kim tarafindan kullanildigini sorgular ve bu sorguyu gelen ip'de yayinlar(Bir nevi broadcast yapar)
def Scan_ARP(user_ipaddress):
    arp_request_packet = scapy.ARP(pdst=user_ipaddress) #ARP paketini olusturmak icin kullanilir. 0'dan 24'e kadar olan ip adreslerini tarar
    broadcast_packed = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast yapacagi yer default olarak dst icinde belirlenmistir
    paket_birlestir = broadcast_packed / arp_request_packet # Gelen 2 paketi karsilastirip birlestirir tek paket haline getirir
                                                            #(Taradigi IP adreslerini Broadcast yapacagi yer ile birlestirir)
    (cevap_gelen, cevaplanamayan) = scapy.srp(paket_birlestir,timeout=1)  # Broadcast'lerden cevap gelenleri dondurur cevap gelmeyenler icin timeout 1 atar ve sonrakine gecer
    cevap_gelen.summary()  # Gelen cevaplar karisik bir sekilde ekrana basilir.Bunu daha duzenli halde gorek icin summary konutu kullanilir

print("Program calisti")
user_input_enter = Create_Object()
Scan_ARP(user_input_enter.ipaddress)
