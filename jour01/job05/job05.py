class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
        print(f"L'age de l'animal {self.age} ans")
    
    def nommer(self, prenom):
        self.prenom = prenom
        print(f"L'animal se nomme {self.prenom}")
        

animal_1 = Animal()
print(f"L'age de l'animal {animal_1.age} ans")
animal_1.vieillir()
animal_1.nommer("Luna")