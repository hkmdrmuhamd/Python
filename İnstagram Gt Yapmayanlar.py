#Takip edilenler ve takipçiler dosyası her zaman instagramdaki son verilere göre yazılmalıdır.İşlem bittikten sonra random dosyası silinmelidir.

with open('Takip.txt', 'r') as file1:
    with open('Takipci.txt', 'r') as file2:
        notsame = set(file1).difference(file2)

notsame.discard('\n')

with open('random.txt', 'w') as file_out:

    for (line) in notsame:
        file_out.write(line)
