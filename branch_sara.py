from branc_main.py import Cioccolato

# class Cioccolato():
#     pass

class Tavoletta(Cioccolato):
    def __init__(self, tipo, percentuale, peso, unità, aggiunte):
        super().__init__(tipo, percentuale)
        self.peso = peso
        self.unità = unità
        if unità < 4:
            self.unità = 4
        elif unità <= 24:
            self.unità = unità
        else:
            unità = 24
        self.aggiunte = aggiunte
        
    def produce(self):
        super().produce()
        print(f" il peso è: {self.peso}")
        print(f" aggiunte: {self.aggiunte}")
        print(f" ha utilizzato queste unita' di cioccolato: {self.unità}")