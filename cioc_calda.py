from branc_main import Cioccolato

class CioccolataCalda(Cioccolato):
    def __init__(self, tipo, percentuale, temperatura, densità):
        super().__init__(tipo, percentuale)
        self.temperatura = temperatura
        self.densità = densità
        
    def produce(self, quantità):
        if quantità >= 20:
            print(f" Il tipo di cioccolato è: {self.tipo} e la percentuale di cacao è: {self.percentuale} ed usa {quantità} unità")
        else:
            print("Quantità non sufficiente")

