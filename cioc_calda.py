from branc_main import Cioccolato

class CioccolataCalda(Cioccolato):
    def __init__(self, tipo, percentuale, temperatura, densità, quantità):
        super().__init__(tipo, percentuale)
        self.temperatura = temperatura
        self.densità = densità
        if quantità >= 20:
            self.quantità = quantità
        else: 
            self.quantità = 20
        

        
    def produce(self):
        print(f" Il tipo di cioccolato è: {self.tipo} e la percentuale di cacao è: {self.percentuale} ed usa {self.quantità} unità")
    

