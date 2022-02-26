class worker:
    def __init__(self,saatlik_ucret,calisma_saati):
        self.saatlik_ucret = saatlik_ucret
        self.calisma_saati = calisma_saati

    def ucretHesaplama(self):
        return self.saatlik_ucret * self.calisma_saati

ucret = int(input("Iscinin saatlik ucreti:"))
calismaSaati = int(input("Iscinin calisma saati:"))
Worker = worker(ucret,calismaSaati)

print("Isciye odenecek miktar: " + str(Worker.ucretHesaplama()))