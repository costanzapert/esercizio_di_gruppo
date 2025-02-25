##Esercizio con Git, fabbrica di cioccolato

#Classe padre con proprieta': tipo cioc, % cioc, Max 100 unita'/day
#Metodo produce(): stampa tipo cioc e % cioc
class Cioccolato:
    def __init__(self, tipo, percentuale):
        self.tipo = tipo
        self.percentuale = percentuale
        max_day = 100
        
    def produce(self):
        print(f" Il tipo di cioccolato è: {self.tipo} e la percentuale di cacao è: {self.percentuale}")