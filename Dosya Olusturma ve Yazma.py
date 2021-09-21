#dosya = open("bilgisayar_muhendisligi.txt","w") w = Eger dosya bulundugumuz dizinde yoksa yeni dosya yaratıp onun icine yazmamızı saglar
                    #w = Eger bulundugumuz dizinde dosya varsa onu silip yerine yeni bir tane acar

#dosya = open("bilgisayar_muhendisligi.txt","r") r = Olan dosyayi acip okumamizi saglar

#dosya = open("bilgisayar_muhendisligi.txt","a") a = Olan bir dosyanin icindeki bilgileri degistirmemizi saglar.Eger dosya yoksa
                                                #yeni dosya acar ve icindekileri degistirmemizi saglar

dosya = open("Dosya olusturma ve yazma.txt","a")
dosya.write("Hello world!")
dosya.write("\nPython Coding")
dosya.close()