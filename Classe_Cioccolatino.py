from Classe_Cioccolato import Cioccolato

class Cioccolatino(Cioccolato):
    def __init__(self, tipo, percentuale, forma, ripieno):
            super().__init__(tipo, percentuale) 
            self.forma = forma
            self.ripieno = ripieno
            unità = 2
            
    def produce(self):
            super().produce()  
            print(f"Forma: {self.forma}, Ripieno: {self.ripieno}")