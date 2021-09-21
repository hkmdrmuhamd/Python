"""
Nobete kalip nobette gecen sure
2 saatten fazlaysa %10 zam
3 saatten fazlaysa %20 zam
4 saat ve uzeri ise %40 zam
"""

maas = float(input("Maasinizi giriniz: "))

nobetteGecenSure = float(input("Nobette kac saat kaldiniz? ->"))

zam = 0

if nobetteGecenSure >=2 and nobetteGecenSure <3:
    zam = maas + (maas *10)/100
elif nobetteGecenSure >=3 and nobetteGecenSure <4:
    zam = maas + (maas *20)/100
elif nobetteGecenSure >=4:
    zam = maas + (maas *40)/100

print("Zamli maasiniz:{}".format(zam))